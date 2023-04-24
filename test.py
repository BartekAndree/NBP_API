import unittest
from main import app


class TestApp(unittest.TestCase):

    def test_get_exchange_rate(self):
        with app.test_client() as client:
            response = client.get('/average-exchange-rate/EUR/2023-01-02')
            self.assertEqual(response.status_code, 200)

    def test_get_max_min_average_value(self):
        with app.test_client() as client:
            response = client.get('/max-min-average-value/USD/30')
            self.assertEqual(response.status_code, 200)

    def test_get_buy_ask_difference(self):
        with app.test_client() as client:
            response = client.get('/buy-ask-difference/GBP/7')
            self.assertEqual(response.status_code, 200)

    def test_invalid_currency_code(self):
        with app.test_client() as client:
            response = client.get('/max-min-average-value/ABC/30')
            self.assertEqual(response.status_code, 400)
            self.assertEqual(response.json, {'error': 'Failed to get exchange rates'})

    def test_invalid_date(self):
        with app.test_client() as client:
            response = client.get('/average-exchange-rate/USD/2022-02-30')
            self.assertEqual(response.status_code, 400)
            self.assertEqual(response.json, {'error': 'Failed to get exchange rate'})

if __name__ == '__main__':
    unittest.main()
