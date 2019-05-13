from flask.views import MethodView
from .mixing import MixinAuthorization
from flask import (
    Blueprint,
    make_response,
    request,
    jsonify
)


class CreditView(MethodView,MixinAuthorization):
    """ Credit View Classs """

    def get(self, *args, **kwargs):
        print(self.is_Authorization(request))
        """ Get all credits """
        return make_response(
            jsonify( 
                { 'wowo': ')' } 
            ),
            200
        )


credit_view = CreditView.as_view('credit_view')