from apps.accounts.models import User
from flask import (
    Blueprint,
    make_response,
    request,
    jsonify
)


class MixinAuthorization(object):
    """"
        Mixin for validate Authorization token 
    """

    def is_Authorization(self,request):
        """
            Validate is a valid token 
        """
        auth_header = request.headers.get('Authorization')
        if auth_header:            
            auth_token = auth_header.split(" ")[0]
        else:
            auth_token = ''
        if auth_token:

            resp = User.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                return True
            return False
        else:
            return False


    def response_auth(self):
        """ 
            Return response status unathorized 
        """
        return make_response(
            jsonify( 
                { 'error': 'HTTP_401_UNAUTHORIZED' } 
            ),
            401
        )        