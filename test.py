from unittest import TestCase
from app import app
import flask
from forex_python.converter import CurrencyRates, CurrencyCodes
codes = CurrencyCodes()
c = CurrencyRates()


class TestApp(TestCase):

    def setUp(self):
        self.client = app.test_client()
        app.config["TESTING"] = True

    def test_main_page(self):
        with self.client as client:
            res = client.get('/')
            html = res.get_data(as_text=True)

        self.assertEqual(res.status_code, 200)
        self.assertIn('<input id="CurrencyFrom" type="text" name="From">', html)

    def test_get_curecy(self):
        with app.test_client() as client:
            res = client.get('/get-currency?from=usd&to=jpy&amount=12')
            data =  flask.request.args
            
        self.assertEqual(res.status_code, 200)
        self.assertIn('Amount', data)
        self.assertIn('From', data)
        self.assertIn('To', data)
    def test_convert(self):
        with self.client as client:
            res = client.get('/get-currency?from=usd&to=usd&amount=12')
            html = res.get_data(as_text=True)
            
        self.assertIn('$: 12.0', html)
           