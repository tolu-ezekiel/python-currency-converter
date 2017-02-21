#!/usr/bin/python

"""
Usage:
    new2.py [--amount=<amount>] [--input_currency=<input_currency>] [--output_currency=<output_currency>] 

Options:
    --amount=<amount>                       Amount
    --input_currency=<input_currency>       inputCurrency
    --output_currency=<output_currency>     outputCurrency
"""

from docopt import docopt
import json

with open('currency_code.json') as data_file:    
    currency_code = json.load(data_file)
    

def check_currency_code(currency_code, currency, total_code):
    for i in range(total_code):
        if currency == currency_code['code'][i]['symbol']:
            currency = currency_code['code'][i]['letter']
            break
    return currency


def main():
    arguments = docopt(__doc__)

    amount = arguments.get('--amount')
    input_currency = arguments.get('--input_currency')
    output_currency = arguments.get('--output_currency')

    total_code =  len(currency_code['code'])
    if input_currency.isalpha() == False or len(input_currency) < 3:
        input_currency = check_currency_code(currency_code, input_currency , total_code)
    if output_currency.isalpha() == False or len(output_currency) < 3:
        output_currency = check_currency_code(currency_code, input_currency , total_code)

    print 'input_currency', input_currency
    print 'output_currency', output_currency


if __name__ == '__main__':
    main()
