import requests
import pprint


# def build_csv(longer_list, shorter_list):
#     res_string = ''

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
    okex_instruments += [instrument['baseCcy'], instrument['quoteCcy']]
okex_set = set(okex_instruments)

binance_instruments = []
response_binance = requests.get(url_binance)
for instrument in response_binance.json()['symbols']:
    binance_instruments += [instrument['baseAsset'], instrument['quoteAsset']]
binance_set = set(binance_instruments)

res_string = ''
res_list = []
res_list_match = []
res_list_no_okex = []
res_list_no_binance = []
for instrument_o in okex_set:
  if instrument_o in binance_set:
    binance_set.remove(instrument_o)
    res_list_match += [[instrument_o, instrument_o, instrument_o]]
  else:
    res_list_no_binance += [[instrument_o, 'absent_in_binance', instrument_o]]
if len(binance_set) > 0:
  for instrument_b in binance_set:
    res_list_no_okex += [[instrument_b, instrument_b, 'absent_in_okex']]

res_list_match.sort()
res_list_no_okex.sort()
res_list_no_binance.sort()
res_list.extend(res_list_match)
res_list.extend(res_list_no_okex)
res_list.extend(res_list_no_binance)
for element in res_list:
    res_string += f'{element[0]},{element[1]},{element[2]}\n'
pprint.pp(res_string)
# pprint.pp(res_list)
with open('test.txt', 'w') as f:
  f.write(res_string)