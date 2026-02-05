# 🕵️ Finding Abductors Using AI

An AI-powered full-stack web application designed to assist in identifying missing persons and potential abductors using image recognition. The system enables users to register cases, upload images, and receive AI-based predictions with confidence scores, supporting authorities and families in investigation workflows.

---

## 📌 Problem Statement

Missing person and abduction cases often suffer from delayed identification and limited technological support in early investigation stages. Manual image matching and verification processes are time-consuming and error-prone. There is a need for a digital platform that can:

- Allow families or citizens to report missing person cases online  
- Enable secure image uploads of suspected individuals  
- Apply AI-based image recognition to assist in identifying potential matches  
- Provide authorities with a centralized dashboard for case monitoring  

This project addresses the above challenges by integrating **AI-driven image analysis** with a **full-stack web platform** to support faster and more reliable identification workflows.

---

## 🚀 What We Achieved

- Built a **full-stack web application** with user and admin workflows for case registration and image uploads  
- Designed and trained a **CNN-based image classification model** for suspect identification  
- Evaluated the model on a dataset of **1,200+ labeled images**, achieving **~85% validation accuracy**  
- Implemented **real-time ML inference** in the backend with confidence scores and “Unknown” class handling  
- Developed a **role-based dashboard** for managing cases and reviewing predictions  
- Containerized the backend and ML service using **Docker**, enabling consistent local setup and deployment  
- Structured the project with modular backend components, database migrations, and RESTful APIs  

---

## 🛠️ Tech Stack

### Backend
- Python  
- Flask (REST APIs)  
- SQLAlchemy + Alembic (Database & migrations)

### Machine Learning
- Custom CNN (TensorFlow / Keras)  
- Image preprocessing & data augmentation  

### Frontend
- HTML  
- CSS  
- JavaScript  

### DevOps / Tooling
- Docker & Docker Compose  
- Git & GitHub  

---


## 📁 **Project File Structure (Current)**

```
Finding-Abductors-Using-AI/
├── README.md
├── abductor_detection_backend/
│   ├── app/
│   │   ├── models/
│   │   ├── routes.py
│   │   ├── templates/
│   │   └── static/
│   ├── cnn/
│   ├── migrations/
│   ├── Dockerfile
│   ├── docker-compose.yml
│   ├── requirements.txt
│   ├── run.py
│   └── train_model.py
└── .gitignore
```

## ⚙️ How to Run (Locally)

```bash
# Clone the repository
git clone https://github.com/Abhinaya-Bolishetti/Finding-Abductors-Using-AI.git
cd Finding-Abductors-Using-AI/abductor_detection_backend

# Install dependencies
pip install -r requirements.txt

# Run the application
python run.py
````

**Using Docker (optional):**

```bash
docker-compose up --build
```

Open in browser:

```
http://localhost:5000
```

---

## 📊 Model Performance

* Dataset: 1,200+ labeled images (public dataset + curated samples)
* Train/Validation Split: 80/20
* Validation Accuracy: ~85%
* Unknown faces are handled by assigning low confidence and labeling them as **“Unknown”** to reduce false positives.

---

## 🔮 Future Enhancements

* Improve model performance with larger and more diverse datasets
* Integrate face embeddings (e.g., FaceNet) for improved recognition
* Add JWT-based authentication and RBAC
* Deploy on cloud (AWS/GCP/Azure)
* Add notifications and audit logs for authorities

---

## 📄 Disclaimer

This project is developed for **academic and learning purposes**. AI predictions are intended to assist investigation workflows and should not be used as the sole basis for real-world law enforcement decisions.
