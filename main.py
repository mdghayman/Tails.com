import os
import json
import requests
from flask import Flask, request
from flask_restful import Resource, Api
from functions import (cache_countries, determine_currency, calculate_rate,
    calculate_output)

if not os.path.isfile('countries_details.txt'):
    cache_countries()
countries_details = json.loads(open('countries_details.txt').read())
customer_country = 'United Kingdom'

input_json = json.loads(open('pricing.json').read())

app = Flask(__name__)
api = Api(app)

class OutputLocal(Resource):
    def get(self):
        return calculate_output(customer_country, input_json)

class OutputForeign(Resource):
    def get(self, country_code):
        for key, value in countries_details['results'].items():
            if country_code == value['alpha3']:
                customer_country = value['name']
        return calculate_output(customer_country, input_json)

class CountryCodes(Resource):
    def get(self):
        country_codes = {}
        for key, value in countries_details['results'].items():
            country_codes[value['alpha3']] = value['name']
        return country_codes

api.add_resource(OutputLocal, '/')
api.add_resource(OutputForeign, '/<string:country_code>/')
api.add_resource(CountryCodes, '/country_codes/')

if __name__ == '__main__':
    app.run(debug=True)
