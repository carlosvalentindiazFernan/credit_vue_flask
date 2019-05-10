from flask_script import Manager
from settings.settings import settings
from apps.common.utils import create_super_user
import os


manager = Manager(
    settings(
        os.getenv('ENVIRONMENT')
    )
)

@manager.command
def createsuperuser():
    """
        Create an user for the app 
    """
    create_super_user()

@manager.command
def migrate():
    """
        Install the sheme data base
    """
    print("run migrations")

if __name__ == '__main__':
    manager.run()