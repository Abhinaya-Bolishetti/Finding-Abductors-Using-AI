from flask_sqlalchemy import SQLAlchemy

# Create a single SQLAlchemy instance
db = SQLAlchemy()

# Import all model classes to register them properly
from .user import User
from .image_record import ImageRecord
