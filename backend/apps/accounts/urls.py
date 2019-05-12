"""
    Here define the urls for the api
"""

from .view import user_view


def register_account_api(app):
    app.add_url_rule(
        '/login/',
        view_func=user_view)