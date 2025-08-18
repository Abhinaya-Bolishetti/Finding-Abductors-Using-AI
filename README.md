# Finding-Abductors-Using-AI 🚨  
AI-powered web system for identifying missing persons using **CNN image recognition**.  

## 📌 Overview  
This project is a **full-stack web portal** for assisting in missing person investigations.  
It allows **citizens, victim families, and police (admins)** to log in, register cases, upload suspicious images, and leverage **AI-based suspect detection**.  

## 🛠 Features  
- 👤 **Multi-user login system**  
  - Citizens → Upload suspicious images  
  - Families → Register missing person cases  
  - Police/Admin → Verify reports and manage cases  
- 📝 **Case registration** with personal details & photo upload  
- 📸 **Image upload** for AI-based CNN recognition  
- 🎨 **Responsive frontend** with HTML, CSS, JavaScript  
- ⚡ **Flask backend** integration ready  
- 🗄 **Database ready** (PostgreSQL/MySQL/SQLite supported)  

## 🗂 Project Structure  
Finding-Abductors-Using-AI/
│── app.py # Flask backend
│── static/
│ ├── style.css # Styling
│ ├── script.js # Frontend scripts
│ ├── main.js, upload.js # Case & image upload logic
│── templates/
│ ├── index.html # Landing page
│ ├── common-login.html # User login
│ ├── register.html # User registration
│ ├── register-case.html # Case registration
│ ├── upload-image.html # Image upload
│ ├── admin-login.html # Police login
│── assets/
│ ├── logo.png
│ ├── background.png
│ ├── ai-theme.png
│ └── missing-person.png
│── requirements.txt # Python dependencies


## 🚀 How to Run  

### 🔧 Setup Backend (Flask)  
1. Clone the repository  
   ```bash
   git clone https://github.com/your-username/Finding-Abductors-Using-AI.git
   cd Finding-Abductors-Using-AI
2.Create a virtual environment
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
3.Install dependencies
pip install -r requirements.txt
4.Run the server
python app.py
5.Open in browser
http://127.0.0.1:5000

