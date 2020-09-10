from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from json import dumps
import datetime

class UserInsuranceOffers(Resource):
    def post(self):
        # define result structure with null values
        result = {
                    'auto': None,
                    'disability': None,
                    'home': None,
                    'life': None
                 }

        # treating when receiving an empty body request
        if request.json != None:
            # get object user sent
            user = request.json
            # defining user`s base risk score
            base_score = 0
            for i in user['risk_questions']:
                base_score += i
            # set initial risk score for each user`s insurance line
            risk_score = {
                'auto': base_score,
                'disability': base_score,
                'home': base_score,
                'life': base_score
             }        
            # get actual year for future comparison
            this_year = datetime.datetime.now().year

            if user['income'] == 0:
                result['disability'] = 'ineligible'
            if len(user['house']) == 0:
                result['home'] = 'ineligible'            
            if len(user['vehicle']) == 0:
                result['auto'] = 'ineligible'

            if user['age'] > 60:
                result['disability'] = 'ineligible'
                result['life'] = 'ineligible'
            elif user['age'] < 30:
                risk_score['auto'] -= 2
                risk_score['disability'] -= 2
                risk_score['home'] -= 2
                risk_score['life'] -= 2
            elif user['age'] >= 30 and user['age'] <= 40:
                risk_score['auto'] -= 1
                risk_score['disability'] -= 1
                risk_score['home'] -= 1
                risk_score['life'] -= 1

            if user['income'] > 200000:
                risk_score['auto'] -= 1
                risk_score['disability'] -= 1
                risk_score['home'] -= 1
                risk_score['life'] -= 1

            if len(user['house']) > 0 and user['house']['ownership_status'] == 'mortgaged':
                risk_score['home'] += 1

            if user['dependents'] > 0:
                risk_score['disability'] += 1
                risk_score['life'] += 1

            if user['marital_status'] == 'married':
                risk_score['disability'] -= 1
                risk_score['life'] += 1

            if len(user['vehicle']) > 0 and this_year - user['vehicle']['year'] <= 5:
                risk_score['auto'] += 1

            # defining user`s final score
            for key in result:
                # only allow final score changing if insurance life wasn`t previously defined as ineligible for user
                if result[key] != 'ineligible':
                    if risk_score[key] <= 0:
                        result[key] = 'economic'
                    elif risk_score[key] > 0 and risk_score[key] < 3:
                        result[key] = 'regular'
                    elif risk_score[key] >= 3:
                        result[key] = 'responsible'                    
                        
        return jsonify(result)
