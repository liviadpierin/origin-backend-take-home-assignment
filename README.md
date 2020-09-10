# Origin Backend Take-Home Assignment
## About the Solution
This solution is intended to resolve [the problem presented by Origin.](https://github.com/OriginFinancial/origin-backend-take-home-assignment)

The API endpoint is responsible for calculating the risk score for each line of insurance that is possible to be available for a user, returning it`s profile.

The solution was build with the following languages and frameworks:
-Python 3.6
-Flask 1.1.2
-Flask RESTful 0.3.8
-Pytest 6.0.1
and a few others found on [requirements.txt](https://github.com/liviadionizio/origin-backend-take-home-assignment/blob/master/requirements.txt)

## Deploy Solution
* Start a container with the command: `docker-compose up -d app`
* The API will run on `http://0.0.0.0:8080`

## How to Use API
Simply make a POST request to `http://0.0.0.0:8080/user-insurance`

## Testing solution
Execute the command `docker-compose exec app pytest tests`
