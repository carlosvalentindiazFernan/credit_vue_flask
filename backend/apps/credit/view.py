from flask.views import MethodView
from .mixing import MixinAuthorization
from flask import (
    Blueprint,
    make_response,
    request,
    jsonify
)

from .models import Credit
from apps import db

class CreditView(MethodView,MixinAuthorization):
    """ Credit View Classs """

    def get(self, *args, **kwargs):
        if self.is_Authorization(request):
            """ Get all credits """

            credits = Credit.query.all()

            return make_response(
                jsonify({
                    "data": [{
                        "id": x.id,
                        "nameCompany": x.name_company, 
                        "numCompany": x.num_company,
                        "credit": x.credit
                    } for x in credits]}
                ),
                200
            )            

        else:
            return self.response_auth()


    def post(self,*arg,**kwargs):
        if self.is_Authorization(request):
            """ Create a credit """

            name = request.data.get('nameCompany')
            number = request.data.get('numberCompany')
            credit = request.data.get('credit')

            if name or number or credit:
                credit = Credit(
                    name = name,
                    numCompany = number,
                    credit = credit
                )

                db.session.add(credit)
                db.session.commit()    
            

                return make_response(
                    jsonify( 
                        { 'created': 'ok' } 
                    ),
                    201
                )

            return make_response(
                jsonify(
                    {'error': 'body request'}
                ),
                400
            )
        else:
            return self.response_auth()
            
        

credit_view = CreditView.as_view('credit_view')