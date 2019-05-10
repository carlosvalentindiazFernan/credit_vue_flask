from flask_api import FlaskAPI
from .config import app_config


def settings(config_name):
    """ Create the app config """

    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    
    return app

