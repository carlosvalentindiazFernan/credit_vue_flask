from flask.views import MethodView
from .models import demos
from flask import (
    Blueprint,
    make_response,
    request,
    jsonify
)

class UserAPI(MethodView):

    def post(self):
        demos()
        print(request.data)
        return "wowo post" 


user_view = UserAPI.as_view('users')