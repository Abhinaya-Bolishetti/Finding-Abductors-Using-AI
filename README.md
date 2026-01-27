# Finding-Abductors-Using-AI 🚨  
AI-powered web system for identifying missing persons using **CNN image recognition**.  

---

## 📌 Overview  
This project is a **web portal** for assisting in missing person investigations.  
It allows **citizens, victim families, and police (admins)** to log in, register cases, upload suspicious images, and leverage **AI-based suspect detection**.  

---

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

---


---
## 🛠 Tech Stack  

### 🌐 Frontend  
- **HTML5, CSS3, JavaScript**  
- Responsive UI design  

### ⚙️ Backend  
- Python (Flask Framework)
- REST API (Flask-Restful)

## 🚀 How to Run  

### 🔧 Setup Backend (Flask)  
```bash
# 1. Clone the repository
git clone https://github.com/your-username/Finding-Abductors-Using-AI.git
cd Finding-Abductors-Using-AI

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the server
python app.py


