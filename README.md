# Finding-Abductors-Using-AI
AI-powered web system for identifying missing persons using CNN image recognition.

## 📌 Overview
This project is a front-end implementation for the **Finding Abductors Using AI** system.  
It allows different user types – citizens, victim families, and police – to log in, submit reports, and upload suspicious images for AI-based suspect detection.

## 🛠 Features
- **Multi-user login system** (Common users, Admin/Police, Victim families)
- **Case registration** with details and photos
- **Image upload** for AI analysis
- Responsive and intuitive UI built with HTML, CSS, and JavaScript
- Backend integration ready via Flask (Python)

## 📂 Project Structure
```
📁 Finding-Abductors-Using-AI
        📁 front
            📄 admin-login.html
            📄 ai-theme.png
            📄 app.py
            📄 background.png
            📄 common-login.html
            📄 common-login.js
            📄 index.html
            📄 location.png
            📄 logo.png
            📄 main.js
            📄 missing-person.png
            📄 register.html
            📄 register-case.html
            📄 script.js
            📄 style.css
            📄 upload.js
            📄 upload-image.html
            📁 .vscode
                📄 launch.json
```

## 🚀 How to Run
1. Download or clone this repository.
2. Open `index.html` (or the relevant HTML file) in your browser for frontend testing.
3. To connect with backend:
   - Ensure Flask server is running (`python app.py`).
   - Update API endpoints in JavaScript files if needed.

## 🧑‍💻 Tech Stack
- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Flask (Python)
- **Database:** PostgreSQL (for backend integration)
- **AI Model:** CNN for image recognition

## 📜 License
This project is for educational and demonstration purposes only.
