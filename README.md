# Currency Exchange Rates API

This is a simple API for retrieving exchange rates for different currencies from the National Bank of Poland (NBP). The API provides endpoints for getting the average exchange rate for a given date and currency code, the maximum and minimum average value for a given currency code and last N quotations, and the largest difference between buy and ask rate for a given currency code and last N quotations.

## Endpoints

### `/average-exchange-rate/<currency_code>/<date>`

Returns the average exchange rate for the given date and currency code.

#### Request parameters

- `currency_code` - The three-letter currency code (e.g. USD, EUR)
- `date` - The date for which to get the exchange rate in the format YYYY-MM-DD

#### Example request

```
GET /average-exchange-rate/USD/2023-04-22
```

#### Example response

```
{
    "date": "2023-04-22",
    "currency": "USD",
    "rate": 3.9512
}
```

### `/max-min-average-value/<currency_code>/<n>`

Returns the maximum and minimum average value for the given currency code and last N quotations.

#### Request parameters

- `currency_code` - The three-letter currency code (e.g. USD, EUR)
- `n` - The number of last quotations to consider

#### Example request

```
GET /max-min-average-value/USD/7
```

#### Example response

```
{
    "currency": "USD",
    "max_rate": 3.9825,
    "min_rate": 3.9378
}
```

### `/buy-ask-difference/<currency_code>/<n>`

Returns the largest difference between buy and ask rate for the given currency code and last N quotations.

#### Request parameters

- `currency_code` - The three-letter currency code (e.g. USD, EUR)
- `n` - The number of last quotations to consider

#### Example request

```
GET /buy-ask-difference/USD/7
```

#### Example response

```
{
    "currency": "USD",
    "max_diff": 0.0191
}
```

## Running the API

To run the API locally, follow these steps:

1. Clone the repository to your local machine
2. Install the required dependencies by running `pip install -r requirements.txt`
3. Start the API by running `python main.py`
4. Navigate to `http://localhost:3000/apidocs` to access the Swagger UI documentation

## Testing the API

To run the tests for the API, follow these steps:

1. Install the required testing dependencies by running `pip install -r requirements-test.txt`
2. Start the API by running `python main.py`
3. In a separate terminal window, run the tests by running `python test.py` 

## Technologies used

- Python 3.9
- Flask
- Flask-RESTful
- Flask-Swagger-UI
- Requests