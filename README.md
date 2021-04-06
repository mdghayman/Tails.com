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

I would generate more tests, to ensure every possible case is covered. Instead, I have only included a few tests here as an illustrative example.

Perhaps this lies outside the scope of this individual challenge, but in practice I would be sure to partner with any internal and external stakeholders early on in the process of developing an API or other component of the data engineering pipeline. This would ensure they play a role in designing, testing, and integrating the component. If such stakeholders will ultimately get more use out of the component than I will, it's essential for them to take ownership and for me to deliver what they demand.

## 3.  What bits did you find the toughest? What bit are you most proud of? In both cases, why?

### Toughest bits

Nothing really pushed me out of my comfort zone. I guess it was tough to know when to stop and hand the test over - while I only spent a few hours and created something good enough, it's important to remember that quick and functional is often better than slow and perfect.

### Proudest bits

I'm most proud of the user interface I created to interact with this app. As discussed below, this approach is hardly efficient or scalable as part of a data engineering pipeline, but it allows for a quick understanding of the tool for a user without having to the think about the code. It could even serve a role in practice, by allowing teams with different priorities and technical backgrounds to visualise the structure and impacts of potential new components in a data engineering pipeline.

## 4.  What one thing could we do to improve this test?

A bit more clarity on how the API would fit into your data pipeline. For example, here I've created a user interface so anybody can generate the desired outputs - using a drag and drop file upload, and dropdown menu selection - making a no code solution that's easy to understand, but the JSON output is probably not useful for the user of the app, and processing JSON inputs as individual text files is not an efficient or scalable mechanism.
