import streamlit as st
import pandas as pd
import os
import json
from functions import cache_countries, price_counter, currency_converter


if not os.path.isfile('countries_details.txt'):
    cache_countries()

countries_list = []
with open('countries_details.txt', 'r') as f:
    countries_details = json.load(f)
    for key, value in countries_details['results'].items():
        countries_list.append(value['name'])

input_file = 'pricing.json'
customer_country = 'local'

st.markdown("<h2 style='text-align: center; color: grey'>\
    Tray.io challenge</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center'>\
    Algorithmically predict the SaaS product that will generate more interest \
    and traffic, to proactively create integrations for unicorns.</p>", \
    unsafe_allow_html=True)

if st.button('Select country for foreign customer'):
    customer_country = st.selectbox(label='Please enter customer country \
        (leave this blank if customer is local)', options=countries_list)

if st.button('Upload new input file'):
    input_file = st.file_uploader('Please drag and drop a text file with your \
        JSON inputs.')

if st.button('Calculate output'):
    if customer_country != 'local':
        st.write(currency_converter(customer_country))
    st.write(price_counter(input_file))
