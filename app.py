from flask import Flask
from flask_restful import Resource, Api
from oer_api import *
import logging

app = Flask(__name__)

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)
api = Api(app)

class LatestExchangeRates(Resource):
    def get(self):
        return {'latest rates': get_latest_exchange_rates()}

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
