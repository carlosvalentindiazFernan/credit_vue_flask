from flask import Flask, jsonify, abort, request, make_response, url_for
from flask_api import FlaskAPI
from flask.views import MethodView
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from .config import app_config
from apps import settings_apps
from apps.credit.urls import register_credit_api
from apps.accounts.urls import register_account_api
from apps.common.view import (
    not_request,
    not_found,
    not_allowed,
    server_error
)

demo ="de"

def settings(config_name):
    """ Create the app config """

    app =settings_apps(app_config[config_name])

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

    return app

