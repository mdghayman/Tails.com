import json
import requests

def cache_countries():
    countries_url = 'https://free.currconv.com/api/v7/countries?' + \
        'apiKey=c6d454bc0e16fa560639'
    countries_details = requests.get(countries_url).json()
    with open('countries_details.txt', 'w') as outfile:
        json.dump(countries_details, outfile)

def currency_converter(customer_country):
    with open('countries_details.txt', 'r') as f:
        countries_details = json.load(f)
    for key, value in countries_details['results'].items():
        if customer_country == value['name']:
            customer_currency = value['currencyId']
    exchange_rate_url = 'https://free.currconv.com/api/v7/convert?q=' + \
        f'GBP_{customer_currency}' + \
        '&compact=ultra&apiKey=c6d454bc0e16fa560639'
    exchange_rate_details = requests.get(exchange_rate_url).json()
    return exchange_rate_details

def price_counter(input_file):
    total_price = 0
    total_vat = 0
    input_text = open(input_file).read()
    input_json = json.loads(input_text)
    details_per_product = {}
    for product in input_json['prices']:
        for key, value in input_json['vat_bands'].items():
            if product['vat_band'] == key:
                product['vat'] = value
        del product['vat_band']
        total_price += product['price']
        total_vat += product['price'] * product['vat']
    return {'total_price': total_price,
        'total_vat': total_vat,
        'products': input_json['prices']}
