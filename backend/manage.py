from flask_script import Manager
from settings.settings import settings
from apps.common.utils import create_super_user
from flask_migrate import Migrate, MigrateCommand
from apps.accounts.models import User
import os


app,db = settings(os.getenv('FLASK_ENV'))

manager = Manager(app)

migrate = Migrate(app, db)
# create an instance of class that will handle our commands
manager = Manager(app)

manager.add_command('db', MigrateCommand)


@manager.command
def createsuperuser():
    """
        Create an user for the app 
    """
    "This function create a super user for the app"

    print("Email")
    email = input()
    print("Password")
    password = input()

    user = User(
        email=email,
        password=password,
        admin=True
    )

    # insert the user

    db.session.add(user)
    db.session.commit()    

    print("User created")


if __name__ == '__main__':
    manager.run()