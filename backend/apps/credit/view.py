from flask.views import View
from flask import (
    Blueprint,
    make_response,
    request,
    jsonify
)


class CreditView(View):
    """ Credit View Classs """

    def get(self, request, *args, **kwargs):
        """ Get all credits """
        return make_response(jsonify({
            'demo': 'asmo'
        })), 200


credit_view = CreditView.as_view('credit_view')