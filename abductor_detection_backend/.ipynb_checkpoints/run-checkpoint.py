import os
import webbrowser
from threading import Timer
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from app import db  # import db from your app package

def create_app():
    app = Flask(
        __name__,
        static_folder=os.path.join(os.getcwd(), 'app', 'static'),
        template_folder=os.path.join(os.getcwd(), 'app', 'templates')
    )

    # Configurations
    app.config['SECRET_KEY'] = 'your_secret_key_here'
    app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key_here'
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://bhavaniboyapati@localhost:5432/abductor_db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'uploads')

    db.init_app(app)
    JWTManager(app)
    CORS(app, resources={r"/*": {"origins": ["http://localhost:5001", "http://127.0.0.1:5001"]}})


    from app.routes import main_bp
    app.register_blueprint(main_bp)
    

    with app.app_context():
        db.create_all()

    return app

def open_chrome():
    chrome_path = "open -a 'Google Chrome' %s"
    webbrowser.get(chrome_path).open("http://127.0.0.1:5001/")

if __name__ == '__main__':
    app = create_app()
    Timer(1, open_chrome).start()
    app.run(host='0.0.0.0', port=5001, debug=True)
