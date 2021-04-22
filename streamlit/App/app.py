import streamlit as st
import os
import json
from functions import cache_countries, currency_converter


if not os.path.isfile('countries_details.txt'):
    cache_countries()

input_file = 'pricing.json'
customer_country = 'United Kingdom'

countries_list = []
with open('countries_details.txt', 'r') as f:
    countries_details = json.load(f)
    for key, value in countries_details['results'].items():
        countries_list.append(value['name'])


col1, col2, col3 = st.beta_columns(3)

col1.markdown("<h3 style='text-align: right; color: purple;'>\
    Michael Hayman</h3>",
    unsafe_allow_html=True)

col1.markdown("<h3 style='text-align: right; color: purple;'>\
    Data Engineer</h3>",
    unsafe_allow_html=True)

col1.markdown("<h3 style='text-align: right; color: purple;'>\
    Coding Test</h3>",
    unsafe_allow_html=True)

col2.image('./images/TailsLogo.png', use_column_width=True)

col3.image('./images/MichaelHayman.jpeg', width=165)


st.markdown("<h2 style='text-align: center; color: grey'>\
    Summary</h2>", unsafe_allow_html=True)

st.markdown("<p style='text-align: center'>\
    The brief required me to recreate a hypothetical version of the internal \
    pricing service at Tails. This is realised here with a simple user \
    interface. The relevant functions are also stored in the python script \
    underlying this app, and so can be intergrated into a wider data pipeline. \
    </p>", unsafe_allow_html=True)


st.markdown("<h3 style='text-align: left; color: grey'>\
    Step 1 (optional): Upload new input file</h3>", unsafe_allow_html=True)

st.markdown("<p style='text-align: left'>\
    The file saved as `pricing.json` in this app directory will be used by \
    default. Any new file uploaded below will be saved as `pricing.json` in \
    this app directory.\
    </p>", unsafe_allow_html=True)

if st.button('Upload new input file'):
    input_file = st.file_uploader('Please drag and drop a text file with your \
        JSON inputs.')


st.markdown("<h3 style='text-align: left; color: grey'>\
    Step 2: Select customer country</h3>", unsafe_allow_html=True)

customer_country = st.selectbox(label='Customer country (leave this blank if \
    customer is from United Kingdom).', options=['<SELECT>']+countries_list)

if customer_country == '<SELECT>':
    customer_country = 'United Kingdom'

st.markdown(f"<p style='text-align: left'>\
    <b>{customer_country}</b> currently selected. \
    </p>", unsafe_allow_html=True)


st.markdown("<h3 style='text-align: left; color: grey'>\
    Step 3: Calculate output</h3>", unsafe_allow_html=True)

st.markdown("<p style='text-align: left'>\
    Click here to see the JSON output. \
    </p>", unsafe_allow_html=True)

if st.button('Calculate output'):
    st.write(currency_converter(input_file, customer_country))
