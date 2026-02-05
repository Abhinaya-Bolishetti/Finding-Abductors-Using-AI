from app import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email_or_mobile = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def to_dict(self):
        return {
            'id': self.id,
            'email_or_mobile': self.email_or_mobile,
            'is_admin': self.is_admin
        }
