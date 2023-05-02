import base64
import os
from datetime import datetime, timedelta
from hashlib import md5
from time import time
from flask import current_app
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from config.config import Config as c


class User(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)

    # Personal info
    first_name = db.Column(db.String(250))
    last_name = db.Column(db.String(250))
    phone_number = db.Column(db.Integer, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(500))
    registration_date = db.Column(db.DateTime, default=datetime.now)
    role = db.Column(db.String(128))
