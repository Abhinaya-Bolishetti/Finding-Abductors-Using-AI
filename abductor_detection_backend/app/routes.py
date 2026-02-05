import os
import uuid
import numpy as np
from flask import Blueprint, request, jsonify, current_app, render_template
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity
)
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

from app.models import db, User, ImageRecord  # Import your models properly

main_bp = Blueprint('main', __name__, template_folder='templates')

# Load CNN model and class labels once at import
model_path = os.path.join('app', 'models', 'your_cnn_model.keras')  # Change filename accordingly
model = load_model(model_path)

labels_path = os.path.join('app', 'models', 'class_labels.txt')
with open(labels_path, 'r') as f:
    CLASS_LABELS = [line.strip() for line in f]

CONFIDENCE_THRESHOLD = 0.5
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(64, 64))  # Match your model input size
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0
    return img_array

def predict_image(model, img_path):
    preprocessed = preprocess_image(img_path)
    preds = model.predict(preprocessed)
    return preds

# Routes

@main_bp.route('/')
def index():
    return render_template('index.html')


@main_bp.route('/upload-image')
def upload_image():
    return render_template('upload-image.html')

@main_bp.route('/common-login', methods=['GET'])
def login_page():
    return render_template('common-login.html')

@main_bp.route('/register', methods=['GET'])
def register_page():
    return render_template('register.html')

@main_bp.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No input data provided'}), 400

    email_or_mobile = data.get('emailOrMobile')
    password = data.get('password')
    confirm_password = data.get('confirmPassword')

    if not email_or_mobile or not password or not confirm_password:
        return jsonify({'error': 'Missing fields'}), 400

    if password != confirm_password:
        return jsonify({'error': 'Passwords do not match'}), 400

    existing_user = User.query.filter_by(email_or_mobile=email_or_mobile).first()
    if existing_user:
        return jsonify({'error': 'User already exists'}), 400

    hashed_password = generate_password_hash(password)
    new_user = User(email_or_mobile=email_or_mobile, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201

@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('common-login.html')

    data = request.get_json() or request.form
    email_or_mobile = data.get('emailOrMobile')
    password = data.get('password')

    if not email_or_mobile or not password:
        return jsonify({'error': 'Missing email/mobile or password'}), 400

    user = User.query.filter_by(email_or_mobile=email_or_mobile).first()
    if not user or not check_password_hash(user.password, password):
        return jsonify({'error': 'Invalid credentials'}), 401

    access_token = create_access_token(identity=user.email_or_mobile)
    return jsonify({"message": "Logged in successfully", "access_token": access_token}), 200

@main_bp.route('/register-case', methods=['GET'])
def register_case():
    return render_template('register-case.html')


@main_bp.route('/upload', methods=['POST'])
@jwt_required()
def upload_image_api():
    if 'image' not in request.files:
        return jsonify({"error": "No image file provided"}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({"error": "Empty filename"}), 400

    if not allowed_file(file.filename):
        return jsonify({"error": "Unsupported file type"}), 400

    upload_folder = current_app.config.get('UPLOAD_FOLDER', 'uploads')
    os.makedirs(upload_folder, exist_ok=True)

    filename = secure_filename(file.filename)
    unique_name = f"{uuid.uuid4().hex}_{filename}"
    file_path = os.path.join(upload_folder, unique_name)
    try:
        file.save(file_path)
    except Exception as e:
        return jsonify({"error": f"Failed to save file: {str(e)}"}), 500

    location = request.form.get('location')
    description = request.form.get('description')

    if not location:
        os.remove(file_path)
        return jsonify({"error": "Location is required"}), 400

    try:
        preds = predict_image(model, file_path)
    except Exception as e:
        os.remove(file_path)
        return jsonify({"error": f"Prediction failed: {str(e)}"}), 500

    predicted_class = int(np.argmax(preds, axis=1)[0])
    confidence = float(np.max(preds))

    predicted_name = (
        CLASS_LABELS[predicted_class]
        if confidence >= CONFIDENCE_THRESHOLD and predicted_class < len(CLASS_LABELS)
        else "Unknown"
    )

    current_user = get_jwt_identity()

    # Save record to DB
    record = ImageRecord(
        filename=unique_name,
        predicted_name=predicted_name,
        confidence=confidence,
        location=location,
        description=description,
        uploaded_by=current_user
    )
    db.session.add(record)
    db.session.commit()

    # Remove file after processing
    os.remove(file_path)

    return jsonify({
        "predicted_class": predicted_class,
        "predicted_name": predicted_name,
        "confidence": confidence
    }), 200
