from flask_sqlalchemy import SQLAlchemy
from flask_api import FlaskAPI

def settings_apps(config):

    app = FlaskAPI(__name__, 
        instance_relative_config=True
    )

    """
        Settings database 
    """

    db = SQLAlchemy(app)
    app.config.from_object(config)


    return app
