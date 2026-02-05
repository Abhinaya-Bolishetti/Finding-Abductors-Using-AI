from . import db  # Correct: importing the db instance from __init__.py

class ImageRecord(db.Model):
    __tablename__ = 'image_records'

    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(120), nullable=False)
    predicted_name = db.Column(db.String(80), nullable=False)
    confidence = db.Column(db.Float, nullable=False)
    location = db.Column(db.String(255), nullable=True)
    description = db.Column(db.Text, nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'filename': self.filename,
            'predicted_name': self.predicted_name,
            'confidence': self.confidence,
            'location': self.location,
            'description': self.description
        }
