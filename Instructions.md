# Coding Test: Pricing Service

Thank you for taking the time to complete our coding test. Your challenge is to
recreate a hypothetical version of our internal pricing service.

You can use any language, framework and/or library for this test. We want to
see how you think about and solve problems in code, so make sure there is a
decent chunk of your own code in there.

Feel free to **spend as much or as little time as you'd like** as long as the
specified functionality is complete. As a ballpark, the test should take around
90 minutes of development time.


## Building the API

Using the [pricing data](./pricing.json), build a RESTful API endpoint that
accepts requests like the one below.

```json
{
    "order": {
        "id": 12345,
        "customer": {},
        "items": [
            {
                "product_id": 1,
                "quantity": 1
            },
            {
                "product_id": 2,
                "quantity": 5
            },
            {
                "product_id": 3,
                "quantity": 1
            }
        ]
    }
}
```

The endpoint should return a data structure which includes:

* the total price for the order
* the total VAT for the order
* the price and VAT for each item in the order

Data structure for the response is up to you.

All monetary values in the `pricing.json` file are in pennies (pound sterling, `GBP`).
The calculated results should be in pennies too.
Any rounding should use standard arithmetic rounding to the nearest penny.


## Going international

In this hypothetical universe we have decided to launch tails.com overseas. We
now want the pricing service to return prices in any currency. Those prices
should be calculated using the latest available exchange rate.

Expand the API to allow a currency to be submitted as part of the request, and
return the prices in that currency. How that currency code is passed in is up
to you.

Use a currency conversion rate API like
[free.currencyconverterapi.com](https://free.currencyconverterapi.com/)
to get the latest exchange rates as part of your solution. (Hint: you might
want to think about how to cache that data).

For the purposes of the test, assume the same VAT rates apply to all countries
and currencies.


## Testing

We would like to see some tests written in the testing framework of your choice
for the pricing logic.

If you do not have time to write tests, tell us how you
would test the pricing logic works as intended. For example: what level of
testing, what sorts of test cases, etc.


## Submitting

Once you are happy with your code, zip it up and email it back to us along with
answers to the following questions:

1. What command(s) do we run to install and start your server?
2. If you had more time, what improvements would you make if any?
3. What bits did you find the toughest? What bit are you most proud of? In both
   cases, why?
4. What one thing could we do to improve this test?
