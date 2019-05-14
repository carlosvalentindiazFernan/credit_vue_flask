from flask.views import MethodView
from flask import (
    Blueprint,
    make_response,
    request,
    jsonify
)
from apps import db
from .models import User

class UserAPI(MethodView):
    """ User View """

    def post(self):
        """ Login User """
        
        user = User.query.filter_by(
            email=request.data['email']
        ).first()

        if user:               
            auth_token = user.encode_auth_token(user.id)        
            if auth_token:
                responseObject = {
                    'Token': auth_token.decode()
                }
                return make_response(jsonify(responseObject)), 200

        return make_response(jsonify({'error': 'invalid user' })), 400
        
 

user_view = UserAPI.as_view('users')