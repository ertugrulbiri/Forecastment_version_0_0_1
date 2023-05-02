from datetime import datetime

from app import db



class User(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)

    # Personal info
    first_name = db.Column(db.String(250))
    last_name = db.Column(db.String(250))
    phone_number = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(500))
    registration_date = db.Column(db.DateTime, default=datetime.now)
    role = db.Column(db.String(128))

    def to_dict(self):
        data = {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'phone_number': self.phone_number,
            'email': self.email,
            'registration_date': self.registration_date,
            'role': self.role
        }
        return data

    def from_dict(self, first_name, last_name, phone_number, password, email):
        setattr(self, 'first_name', first_name)
        setattr(self, 'last_name', last_name)
        setattr(self, 'phone_number', phone_number)
        setattr(self, 'email', email)
        setattr(self, 'password', password)