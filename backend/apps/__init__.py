# app/__init__.py

from flask_sqlalchemy import SQLAlchemy
from flask_api import FlaskAPI
from flask_bcrypt import Bcrypt

# initialize db
db = SQLAlchemy()

app = FlaskAPI(__name__, 
    instance_relative_config=True
)

bcrypt = Bcrypt(app)

