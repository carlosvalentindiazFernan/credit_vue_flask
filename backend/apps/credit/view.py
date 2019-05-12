from flask.views import MethodView
from flask import (
    Blueprint,
    make_response,
    request,
    jsonify
)


class CreditView(MethodView):
    """ Credit View Classs """

    def get(self, *args, **kwargs):
        """ Get all credits """
        return make_response(
            jsonify( 
                { 'wowo': ')' } 
            ),
            200
        )


credit_view = CreditView.as_view('credit_view')