# API orchestrator
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from json import dumps

from .classes.user_insurance_offers import UserInsuranceOffers

app = Flask(__name__)
api = Api(app)

# register routes
api.add_resource(UserInsuranceOffers, '/user-insurance') 

if __name__ == '__main__':
    app.run(host='0.0.0.0')    
