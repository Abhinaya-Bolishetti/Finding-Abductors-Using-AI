from flask import Flask, request
from flask_cors import CORS
import psycopg2
import bcrypt

app = Flask(__name__)
CORS(app)

# PostgreSQL DB connection
conn = psycopg2.connect(
    dbname="your_db_name",
    user="your_user",
    password="your_password",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# Create users table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    email_or_mobile TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL
)
''')
conn.commit()

@app.route('/register', methods=['POST'])
def register():
    data = request.form
    email_or_mobile = data.get('emailOrMobile')
    password = data.get('password')
    confirm = data.get('confirmPassword')

    if not email_or_mobile or not password or not confirm:
        return "All fields are required", 400

    if password != confirm:
        return "Passwords do not match", 400

    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    try:
        cursor.execute("INSERT INTO users (email_or_mobile, password_hash) VALUES (%s, %s)",
                       (email_or_mobile, hashed))
        conn.commit()
        return "Registration successful"
    except psycopg2.IntegrityError:
        conn.rollback()
        return "User already exists", 400

@app.route('/login', methods=['POST'])
def login():
    data = request.form
    email_or_mobile = data.get('emailOrMobile')
    password = data.get('password')

    cursor.execute("SELECT password_hash FROM users WHERE email_or_mobile = %s", (email_or_mobile,))
    result = cursor.fetchone()

    if result:
        stored_hash = result[0]
        if bcrypt.checkpw(password.encode('utf-8'), stored_hash.encode('utf-8')):
            return "Login successful"
        else:
            return "Incorrect password", 401
    else:
        return "User not found", 404

if __name__ == '__main__':
    app.run(port=5001, debug=True)
