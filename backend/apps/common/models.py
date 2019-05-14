from apps import db
import datetime



class Country(db.Model):
    """ Country Model  """
    __tablename__ = "country"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)


    def __init__(self, name):
        """Initialize the country ."""
        self.name = name
        self.registered_on = datetime.datetime.now()
