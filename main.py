from flask import Flask
from flask_restful import Resource, Api
from flask_swagger_ui import get_swaggerui_blueprint
import requests

app = Flask(__name__)

SWAGGER_URL = '/apidocs'  # URL for exposing Swagger UI
API_URL = '\static\swagger.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL
)
app.register_blueprint(swaggerui_blueprint)

api = Api(app)


def get_exchange_rate(date, currency_code):
    """
    Returns average exchange rate for the given date and currency code
    """
    url = f"https://api.nbp.pl/api/exchangerates/rates/A/{currency_code}/{date}/"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        rate = data["rates"][0]["mid"]
        return {"date": date, "currency": currency_code, "rate": rate}, 200
    else:
        return {"error": "Failed to get exchange rate"}, 400

def get_max_min_average_value(currency_code, n):
    """
    Returns max and min average value for the given currency code and last N quotations
    """
    url = f"https://api.nbp.pl/api/exchangerates/rates/A/{currency_code}/last/{n}/?format=json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        rates = [d["mid"] for d in data["rates"]]
        max_rate = max(rates)
        min_rate = min(rates)
        return {"currency": currency_code, "max_rate": max_rate, "min_rate": min_rate}, 200
    else:
        return {"error": "Failed to get exchange rates"}, 400

def get_buy_ask_difference(currency_code, n):
    """
    Returns the largest difference between buy and ask rate for the given currency code and last N quotations
    """
    url = f"https://api.nbp.pl/api/exchangerates/rates/C/{currency_code}/last/{n}/?format=json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        diffs = [d["ask"] - d["bid"] for d in data["rates"]]
        max_diff = max(diffs)
        return {"currency": currency_code, "max_diff": max_diff}, 200
    else:
        return {"error": "Failed to get exchange rates"}, 400
    
class AverageExchangeRate(Resource):
    def get(self, date, currency_code):
        return get_exchange_rate(date, currency_code)

class MaxMinAverageValue(Resource):
    def get(self, currency_code, n):
        return get_max_min_average_value(currency_code, n)
    
class BuyAskDifference(Resource):
    def get(self, currency_code, n):
        return get_buy_ask_difference(currency_code, n)

api.add_resource(AverageExchangeRate, '/average-exchange-rate/<currency_code>/<date>')
api.add_resource(MaxMinAverageValue, '/max-min-average-value/<currency_code>/<n>')
api.add_resource(BuyAskDifference, '/buy-ask-difference/<currency_code>/<n>')

if __name__ == '__main__':
    app.run(debug=True)