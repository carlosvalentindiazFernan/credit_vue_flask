from apps import db
import datetime

class Credit(db.Model):
    """ Credit Model for storing credit related details """
    __tablename__ = "credit"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name_company = db.Column(db.String(255), nullable=False)
    num_company = db.Column(db.String(255), nullable=False)
    credit = db.Column(db.Float, nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)


    def __init__(self, name, numCompany,credit):
        """Initialize the user with an email and a password."""
        self.name = name
        self.num_company = numCompany
        self.credit = credit
        self.registered_on = datetime.datetime.now()
