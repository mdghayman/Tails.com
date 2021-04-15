import os
import json
import requests
from flask import Flask, request
from flask_restful import Resource, Api
from functions import (cache_countries, determine_currency, calculate_rate,
    calculate_output)

if not os.path.isfile('countries_details.txt'):
    cache_countries()

app = Flask(__name__)
api = Api(app)

class OutputLocal(Resource):
    def get(self):
        customer_country = 'United Kingdom'
        input_json = json.loads(open('pricing.json').read())
        return calculate_output(customer_country, input_json)

class OutputForeign(Resource):
    def get(self, country_code):
        countries_details = json.loads(open('countries_details.txt').read())
        for key, value in countries_details['results'].items():
            if country_code == value['alpha3']:
                customer_country = value['name']
        input_json = json.loads(open('pricing.json').read())
        return calculate_output(customer_country, input_json)

api.add_resource(OutputLocal, '/')
api.add_resource(OutputForeign, '/<string:country_code>')

if __name__ == '__main__':
    app.run(debug=True)
