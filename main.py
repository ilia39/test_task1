import requests
import pprint


def build_csv(longer_list, shorter_list):
    res_string = ''

REQ_CONST_OKEX = 'https://www.okex.com'
REQ_CONST_BINANCE = 'https://api.binance.com'
req_method_okex = '/api/v5/public/instruments'
req_method_binance = '/api/v3/exchangeInfo'
url_binance = REQ_CONST_BINANCE + req_method_binance
url_okex = REQ_CONST_OKEX + req_method_okex
params_okex = {
    'instType': 'SPOT'
}

okex_instruments = []
response_okex = requests.get(url_okex, params=params_okex)
for instrument in response_okex.json()['data']:
    okex_instruments += [[instrument['instId'], instrument['baseCcy'], instrument['quoteCcy']]]

binance_instruments = []
response_binance = requests.get(url_binance)
for instrument in response_binance.json()['symbols']:
    binance_instruments += [[instrument['symbol'], instrument['baseAsset'], instrument['quoteAsset']]]

with open('response_okex.txt', 'w') as f:
    f.write(str(okex_instruments))
with open('response_binance.txt', 'w') as f:
    f.write(str(binance_instruments))