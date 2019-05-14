from flask_bcrypt import Bcrypt
from apps import db
import datetime
import os
import jwt
import datetime



class User(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)


    def __init__(self, email, password,admin):
        """Initialize the user with an email and a password."""
        self.email = email
        self.password = Bcrypt().generate_password_hash(password).decode()
        self.registered_on = datetime.datetime.now()
        self.admin = admin


    @staticmethod
    def decode_auth_token(auth_token):
        """
            Decodes the auth token
        """

        try:
            payload = jwt.decode(auth_token, os.getenv('SECRET'))
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'


    def encode_auth_token(self, user_id):
        """
        Generates the Auth Token
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=500),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(
                payload,
                str(os.getenv('SECRET')),
                algorithm='HS256'
            )
        except Exception as e:
            print(e)
            return e