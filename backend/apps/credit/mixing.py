from apps.accounts.models import User

class MixinAuthorization(object):

    def is_Authorization(self,request):
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