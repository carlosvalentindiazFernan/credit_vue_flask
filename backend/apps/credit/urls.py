"""
    Here define the urls for the api
"""

from .view import credit_view
from . import credit_blueprint


credit_blueprint.add_url_rule(
    '/',
    view_func=credit_view,
    methods=['GET'])