"""
    Here define the urls for the api
"""

from .view import credit_view
from .routes import credit_blueprint

def register_credit_api(app):
    app.add_url_rule(
        '/credits/',
        view_func=credit_view)