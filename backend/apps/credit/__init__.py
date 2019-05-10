from flask import Blueprint

credit_blueprint = Blueprint('credits', __name__)

from . import urls
