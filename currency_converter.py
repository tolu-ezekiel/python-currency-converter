#!/usr/bin/python

"""
Usage:
    currency_converter.py [--amount=<amount>] [--input_currency=<input_currency>] [--output_currency=<output_currency>] 

Options:
    --amount=<amount>                       Amount
    --input_currency=<input_currency>       inputCurrency
    --output_currency=<output_currency>     outputCurrency
"""

from docopt import docopt
import json
import requests

with open('currency_code.json') as data_file:    
    currency_code = json.load(data_file)
    
def check_currency_code(currency_code, currency, total_code):
    for i in range(total_code):
        if unicode(currency, "utf-8") == currency_code['code'][i]['symbol']:
            currency = currency_code['code'][i]['letter']
            break
    return currency

def convert_currency(input_currency, output_currency, amount):
    token = "0EFC588CBFB84BE9B5E63D7372B6B719"
    r = requests.get('http://globalcurrencies.xignite.com/xGlobalCurrencies.json/ConvertRealTimeValue?_token='+ token +'&From='+ input_currency +'&To=' + output_currency +'&Amount=' + amount)
    if json.loads(r.content)['Outcome'] == 'Success':
        conversion_result = json.loads(r.content)['Result']
        return conversion_result
    else:
        return json.loads(r.content)['Outcome']

def main():
    arguments = docopt(__doc__)
    amount = arguments.get('--amount')
    input_currency = arguments.get('--input_currency')
    output_currency = arguments.get('--output_currency')

    total_code =  len(currency_code['code'])
    if input_currency.isalpha() == False or len(input_currency) < 3:
        input_currency = check_currency_code(currency_code, input_currency , total_code)
    result = {
        "input": {
            "amount": amount,
            "currency": str(input_currency)
        },
        "output": {
        }
    }
    if output_currency:
        if output_currency.isalpha() == False or len(output_currency) < 3:
            output_currency = check_currency_code(currency_code, output_currency , total_code)
        conversion_result = convert_currency(input_currency, output_currency, amount)
        result['output'].update({str(output_currency): conversion_result})
        print result
    else:
        for i in range(total_code):
            output_currency = currency_code['code'][i]['letter']
            if output_currency != input_currency:
                conversion_result = convert_currency(input_currency, output_currency, amount)
                result['output'].update({str(output_currency): conversion_result})
        print result


if __name__ == '__main__':
    main()
