import os
import json
import unittest
import requests
from functions import (cache_countries, determine_currency, calculate_rate,
    calculate_output)

api_key = 'c6d454bc0e16fa560639'

if not os.path.isfile('countries_details.txt'):
    cache_countries()
countries_details = json.loads(open('countries_details.txt').read())
customer_country = 'United Kingdom'

input_json = json.loads(open('pricing.json', 'r').read())

class test_cache_countries_output(unittest.TestCase):
    def test_output(self):
        self.assertEqual(type(cache_countries()), dict)

class test_determine_currency_output(unittest.TestCase):
    def test_output(self):
        self.assertEqual(type(determine_currency(customer_country)), str)

class test_calculate_rate_example_EUR(unittest.TestCase):
    def test_output(self):
        customer_currency = 'EUR'
        self.assertEqual(type(calculate_rate(customer_currency)), float)

class test_calculate_output(unittest.TestCase):
    def test_output(self):
        self.assertEqual(type(calculate_output(customer_country, input_json))\
        , dict)

class test_api_countries_http_response(unittest.TestCase):
    def test_ouput(self):
        api_key = 'c6d454bc0e16fa560639'
        countries_url = 'https://free.currconv.com/api/v7/countries?' + \
            f'apiKey={api_key}'
        response = requests.get(countries_url)
        self.assertEqual(response.status_code, 200)

class test_api_exchange_rate_gbp_http_response(unittest.TestCase):
    def test_ouput(self):
        exchange_rate_url = 'https://free.currconv.com/api/v7/convert?q=' + \
        f'GBP_GBP' + \
        '&compact=ultra&' + \
        f'apiKey={api_key}'
        response = requests.get(exchange_rate_url)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
