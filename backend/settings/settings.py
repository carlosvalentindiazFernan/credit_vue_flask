from flask import Flask, jsonify, abort, request, make_response, url_for
from flask_api import FlaskAPI
from flask.views import MethodView
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt

from .config import app_config
from apps.credit.urls import register_credit_api
from apps.accounts.urls import register_account_api
from apps.common.view import (
    not_request,
    not_found,
    not_allowed,
    server_error
)
from apps import db


def settings(config_name):
    """ Create the app config """

    app = FlaskAPI(__name__, 
        instance_relative_config=True
    )

    app.config.from_object(app_config[config_name])

    """
        Settings database 
    """
    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    bcrypt = Bcrypt(app)


    """
        Settings cors
    """
    CORS(app)
    
    """
        Here register blueprint and routes
    """

    register_credit_api(app)
    register_account_api(app)


    app.register_error_handler(404, not_found)
    app.register_error_handler(400, not_request)
    app.register_error_handler(500, server_error)
    app.register_error_handler(405, not_allowed)

    return (
        app,
        db
    )

