from flask import Flask
from flask_restful import Resource, Api
from oer_api import *


def create_app():
    app = Flask(__name__)

    api = Api(app)

    class LatestExchangeRates(Resource):
        def get(self):
            return {'latest rates': get_latest_exchange_rates()}

    ##Accepts date in mm-dd-yyy format separated with dashes (-)
    class HistoricalExchangeRates(Resource): 
        def get(self, date):
            if validate_date_format(date) == 0:
                return {'error' : 'Incorrect date format, please enter a date in MM-DD-YYYY.'}

            if is_valid_date(date): 
                date = datetime.datetime.strptime(date, "%m-%d-%Y").strftime("%Y-%m-%d")
                return {'historical rates': get_historical_exchange_rates(date)}
            else:
                return {'error' : 'The entered date is not valid for a historical lookup.'}
            

    api.add_resource(LatestExchangeRates, '/latest')
    api.add_resource(HistoricalExchangeRates, '/historical/<string:date>')

create_app()
