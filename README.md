# Data Engineer Coding Test for Tails.com
### Michael Hayman, 6 April 2021

## 1.  What command(s) do we run to install and start your server?

### Starting the server

1. Store this repo on your hard drive, either by opening the zip file sent to you, or by downloading or cloning from GitHub.
2. In your command line, change directory to navigate to this repo.
3. In your command line, run the command `pip install -r requirements.txt`. You may instead need to run `pip3 install -r requirements.txt`, depending on your environment. This assumes that Python and pip are already install in your environment, but if not you can follow these instructions for Python3 `https://www.python.org/downloads/` and then these instructions for pip `https://pip.pypa.io/en/stable/installing/`.
6. Run the command `python main.py` in your command line. The server will now be running on `http://127.0.0.1:5000/`.

### Using the API

1. To return output for a local (United Kingdom) customer: `http://127.0.0.1:5000/`.
2. To return output for a customer from country with three letter code `XXX`: `http://127.0.0.1:5000/XXX/`.
3. If the country code is unknown, the dictionary containing all country names and codes can be found at `http://127.0.0.1:5000/XXX/country_codes/`.
4. The output includes `customer_country`, `customer_currency`, `exchange_rate`, `total_price_GBP`, `total_vat_GBP`, and for each product includes `product_id`, `price_GBP`, and `vat`. If `customer_country` is not `United Kingdom`, the output will also include `customer_currency` amounts for `total price`, `total vat`, and `price` for each product.
5. The file named `pricing.json` will be used as input.

## 2.  If you had more time, what improvements would you make if any?

I would generate more tests, to ensure every possible case is covered - I have only included a few tests here as an illustrative example. Also, while it lies outside the scope of this test, in practice I would be sure to partner with any internal and external stakeholders early on in the process of developing an API or other component of the data engineering pipeline. This would ensure they play a role in designing, testing, and integrating the component. If such stakeholders will ultimately get more use out of the component than I will, it's essential for them to take ownership and for me to deliver what they demand.

## 3.  What bits did you find the toughest? What bit are you most proud of? In both cases, why?

### Toughest bits

Understanding exactly what was required from the test - very much a conceptual and isolated API. It would be easier if I could see how the data inputs and outputs would fit together, but in this simple example there's only a text file input and JSON output at a URL. This led me to overthink the problem and build a frontend initially for completeness, and in doing so I used Streamlit to shortcut the backend, but upon realising this mistake I could simply build a Flask backend.

### Proudest bits

I'm proud when reflecting on the wide range of skills I've been improving in recent months. As I haven't worked as in a data engineer role in a company with a large complete data team, I haven't had to build APIs that would be used by other stakeholders, but it was an easy task once I realised that I was overthinking it and building an API in Flask was like a simplified version of building an app backend in Flask.

## 4.  What one thing could we do to improve this test?

A bit more clarity on how the API would fit into your data pipeline. For example, I've assumed the input is read from the text file included in the challenge repo on GitHub, but this wouldn't make much sense in a production environment. Instead, the test could specify some kind of service that passes the pricing data into the API - this might make things more complicated for the sake of the challenge, but could generate some fun and realistic integrated solutions.
