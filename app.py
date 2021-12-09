from flask import Flask, render_template, request, flash, redirect, url_for
from forex_python.converter import CurrencyRates, CurrencyCodes
from check_valid import validity

valid = validity

currency_rates = CurrencyRates()
currency_codes = CurrencyCodes()

app = Flask(__name__)


@app.route('/')
def main_page():
    """send to main page"""
    return render_template('index.html')

@app.route('/get-currency')
def requested_currency():
    """receive values from form and render results"""
    # print(request.args)
    from_currency = request.args['CurrencyFrom'].upper()
    to_currency = request.args['CurrencyTo'].upper()
    amount = request.args['Amount']

    USDrates = currency_rates.get_rates('USD')
    
    errorsList = validity(currency_rates, from_currency, to_currency, amount)
    if len(errorsList) > 0:
        for err in errorsList:
            flash(f"{err}")
        return redirect(url_for('main_page'))
    

    cymbol = currency_codes.get_symbol(to_currency)
    convert = USDrates.convert(from_currency, to_currency, float(amount))
    convert = round(convert, 2)
    
    return render_template('result.html', convert=convert, symbol=cymbol)
   
    