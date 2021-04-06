# Data Engineer Coding Test for Tails.com
### Michael Hayman, 6 April 2021

## 1.  What command(s) do we run to install and start your server?

### Starting the app
1. Store this repo on your hard drive, either by opening the zip file sent to you, or by downloading or cloning from GitHub.
2. If you do not have Streamlit installed, then install it with the command `pip install streamlit` (this assumes Python3 and pip are installed in your environment, but if not you can follow these `instructions for Python3 [https://www.python.org/downloads/]` and then these `instructions for pip [https://pip.pypa.io/en/stable/installing/]`).
3. Navigate to the folder containing the Streamlit app file (e.g. if your pwd contains this repo `Tails.com`, enter `cd Tails.com/app` in your command line).
5. Run the streamlit app, with the command `streamlit run app.py`.
6. View the app on your browser, with the URL `http://localhost:8501`.

### Using the app
The app's user interface contains three simple steps. Once you have followed the above instructions to start the app, follow these steps to use it.
1. You may drag and drop a new input file directly into the app. Your new file will then be stored as `pricing.json` and will be used in the model. By default, the model will always use the file save as `pricing.json` within the `app` folder as input.
2. You may select the customer's country. Clicking on the box here opens a dropdown menu with every country listed at `https://free.currencyconverterapi.com/`. You may type the first few letters of the country here to navigate quickly to your country of choice. Once the customer country is selected, this will effect the state of the app and therefore its outputs, until you refresh the page. The customer country is `United Kingdom` by default, and will remain so if you do not interact with this step.
3. Simply click the `Calculate output` button to generate the desired JSON output. This output includes `customer_country`, `customer_currency`, `exchange_rate`, `total_price_GBP`, `total_vat_GBP`, and for each product includes `product_id`, `price_GBP`, and `vat`. If `customer_country` is not `United Kingdom`, the output will also include `customer_currency` amounts for `total price`, `total vat`, and `price` for each product.

## 2.  If you had more time, what improvements would you make if any?
## 3.  What bits did you find the toughest? What bit are you most proud of? In both cases, why?
## 4.  What one thing could we do to improve this test?
