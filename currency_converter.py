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
    

def main():
    arguments = docopt(__doc__)

    amount = arguments.get('--amount')
    input_currency = arguments.get('--input_currency')
    output_currency = arguments.get('--output_currency')

    print 'amount', amount
    print 'input_currency', input_currency
    print 'output_currency', output_currency

if __name__ == '__main__':
    main()