import requests
import json

def test_post():
    url = 'http://0.0.0.0:8080/user-insurance'

    # Additional headers
    headers = {'Content-Type': 'application/json'}

    # Body
    payload = {
                'age': 35,
                'dependents': 2,
                'house': {'ownership_status': 'owned'},
                'income': 0,
                'marital_status': 'married',
                'risk_questions': [0, 1, 0],
                'vehicle': {'year': 2018}
              }

    # convert dict to json
    response = requests.post(url, headers=headers, data=json.dumps(payload,indent=4))

    # Validade response contents (headers and body)
    assert response.status_code == 200
    assert json.loads(response.text) == {
                                            'auto': 'regular',
                                            'disability': 'ineligible',
                                            'home': 'economic',
                                            'life': 'regular'
                                        }
