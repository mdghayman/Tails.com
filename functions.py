import json
import requests


api_key = 'c6d454bc0e16fa560639'


def cache_countries():

    countries_url = 'https://free.currconv.com/api/v7/countries?' + \
        f'apiKey={api_key}'

    countries_details = requests.get(countries_url).json()

    with open('countries_details.txt', 'w') as outfile:
        json.dump(countries_details, outfile)

    return countries_details


def currency_converter(input_file, customer_country):

    customer_currency = 'GBP'

    with open('countries_details.txt', 'r') as f:
        countries_details = json.load(f)

    for key, value in countries_details['results'].items():
        if customer_country == value['name']:
            customer_currency = value['currencyId']

    exchange_rate_code = f'GBP_{customer_currency}'

    exchange_rate_url = 'https://free.currconv.com/api/v7/convert?q=' + \
        f'GBP_{customer_currency}' + \
        '&compact=ultra&' + \
        f'apiKey={api_key}'

    exchange_rate_details = requests.get(exchange_rate_url).json()
    exchange_rate = exchange_rate_details[exchange_rate_code]

    total_price_GBP = 0
    total_vat_GBP = 0
    total_price_customer_currency = 0
    total_vat_customer_currency = 0
    input_text = open(input_file).read()
    input_json = json.loads(input_text)
    details_per_product = {}

    for product in input_json['prices']:
        product['price_GBP'] = product['price']
        product[f'price_{customer_currency}'] = round(product['price'] * exchange_rate)
        del product['price']
        for key, value in input_json['vat_bands'].items():
            if product['vat_band'] == key:
                product['vat'] = value
        del product['vat_band']
        total_price_GBP += product['price_GBP']
        total_vat_GBP += product['price_GBP'] * product['vat']
        total_price_customer_currency += product[f'price_{customer_currency}']
        total_vat_customer_currency += product[f'price_{customer_currency}'] * product['vat']

    return {'customer_country': customer_country,
        'customer_currency': customer_currency,
        'exchange_rate': exchange_rate,
        'total_price_GBP': total_price_GBP,
        'total_vat_GBP': round(total_vat_GBP),
        f'total_price_{customer_currency}': total_price_customer_currency,
        f'total_vat_{customer_currency}': round(total_vat_customer_currency),
        'products': input_json['prices'],
    }
