# from datetime import date, date, timedelta
# today = date.today()
# print(today + timedelta(days=1))


d = {'date': '12.02.2023', 'bank': 'PB', 'baseCurrency': 980, 'baseCurrencyLit': 'UAH', 'exchangeRate': [{'baseCurrency': 'UAH', 'currency': 'AUD', 'saleRateNB': 25.5377, 'purchaseRateNB': 25.5377}, {'baseCurrency': 'UAH', 'currency': 'AZN', 'saleRateNB': 21.5464, 'purchaseRateNB': 21.5464}, {'baseCurrency': 'UAH', 'currency': 'BYN', 'saleRateNB': 13.2919, 'purchaseRateNB': 13.2919}, {'baseCurrency': 'UAH', 'currency': 'CAD', 'saleRateNB': 27.3012, 'purchaseRateNB': 27.3012}, {'baseCurrency': 'UAH', 'currency': 'CHF', 'saleRateNB': 39.8286, 'purchaseRateNB': 39.8286, 'saleRate': 43.11, 'purchaseRate': 39.6}, {'baseCurrency': 'UAH', 'currency': 'CNY', 'saleRateNB': 5.3961, 'purchaseRateNB': 5.3961}, {'baseCurrency': 'UAH', 'currency': 'CZK', 'saleRateNB': 1.6619, 'purchaseRateNB': 1.6619, 'saleRate': 1.795, 'purchaseRate': 1.65}, {'baseCurrency': 'UAH', 'currency': 'DKK', 'saleRateNB': 5.2916, 'purchaseRateNB': 5.2916}, {'baseCurrency': 'UAH', 'currency': 'EUR', 'saleRateNB': 39.3826, 'purchaseRateNB': 39.3826, 'saleRate': 42.4, 'purchaseRate': 41.4}, {'baseCurrency': 'UAH', 'currency': 'GBP', 'saleRateNB': 44.4784, 'purchaseRateNB': 44.4784, 'saleRate': 48.2, 'purchaseRate': 44.27}, {'baseCurrency': 'UAH', 'currency': 'GEL', 'saleRateNB': 13.7948, 'purchaseRateNB': 13.7948}, {'baseCurrency': 'UAH', 'currency': 'HUF', 'saleRateNB': 0.102036, 'purchaseRateNB': 0.102036}, {'baseCurrency': 'UAH', 'currency': 'ILS', 'saleRateNB': 10.4856, 'purchaseRateNB': 10.4856}, {'baseCurrency': 'UAH', 'currency': 'JPY', 'saleRateNB': 0.27961, 'purchaseRateNB': 0.27961}, {'baseCurrency': 'UAH', 'currency': 'KZT', 'saleRateNB': 0.080877, 'purchaseRateNB': 0.080877}, {'baseCurrency': 'UAH', 'currency': 'MDL', 'saleRateNB': 1.9487, 'purchaseRateNB': 1.9487}, {'baseCurrency': 'UAH', 'currency': 'NOK', 'saleRateNB': 3.6092, 'purchaseRateNB': 3.6092}, {'baseCurrency': 'UAH', 'currency': 'PLN', 'saleRateNB': 8.3101, 'purchaseRateNB': 8.3101, 'saleRate': 8.9, 'purchaseRate': 8.17}, {'baseCurrency': 'UAH', 'currency': 'SEK', 'saleRateNB': 3.5312, 'purchaseRateNB': 3.5312}, {'baseCurrency': 'UAH', 'currency': 'SGD', 'saleRateNB': 27.6616, 'purchaseRateNB': 27.6616}, {'baseCurrency': 'UAH', 'currency': 'TMT', 'saleRateNB': 10.4482, 'purchaseRateNB': 10.4482}, {'baseCurrency': 'UAH', 'currency': 'TRY', 'saleRateNB': 1.9417, 'purchaseRateNB': 1.9417}, {'baseCurrency': 'UAH', 'currency': 'UAH', 'saleRateNB': 1.0, 'purchaseRateNB': 1.0}, {'baseCurrency': 'UAH', 'currency': 'USD', 'saleRateNB': 36.5686, 'purchaseRateNB': 36.5686, 'saleRate': 39.8, 'purchaseRate': 39.3}, {'baseCurrency': 'UAH', 'currency': 'UZS', 'saleRateNB': 0.0032448, 'purchaseRateNB': 0.0032448}, {'baseCurrency': 'UAH', 'currency': 'XAU', 'saleRateNB': 68822.11, 'purchaseRateNB': 68822.11}]}
c = ['EUR', 'USD']

def represent(cur=[]):
    d = {'date': '12.02.2023', 'bank': 'PB', 'baseCurrency': 980, 'baseCurrencyLit': 'UAH',
         'exchangeRate': [{'baseCurrency': 'UAH', 'currency': 'AUD', 'saleRateNB': 25.5377, 'purchaseRateNB': 25.5377},
                          {'baseCurrency': 'UAH', 'currency': 'AZN', 'saleRateNB': 21.5464, 'purchaseRateNB': 21.5464},
                          {'baseCurrency': 'UAH', 'currency': 'BYN', 'saleRateNB': 13.2919, 'purchaseRateNB': 13.2919},
                          {'baseCurrency': 'UAH', 'currency': 'CAD', 'saleRateNB': 27.3012, 'purchaseRateNB': 27.3012},
                          {'baseCurrency': 'UAH', 'currency': 'CHF', 'saleRateNB': 39.8286, 'purchaseRateNB': 39.8286,
                           'saleRate': 43.11, 'purchaseRate': 39.6},
                          {'baseCurrency': 'UAH', 'currency': 'CNY', 'saleRateNB': 5.3961, 'purchaseRateNB': 5.3961},
                          {'baseCurrency': 'UAH', 'currency': 'CZK', 'saleRateNB': 1.6619, 'purchaseRateNB': 1.6619,
                           'saleRate': 1.795, 'purchaseRate': 1.65},
                          {'baseCurrency': 'UAH', 'currency': 'DKK', 'saleRateNB': 5.2916, 'purchaseRateNB': 5.2916},
                          {'baseCurrency': 'UAH', 'currency': 'EUR', 'saleRateNB': 39.3826, 'purchaseRateNB': 39.3826,
                           'saleRate': 42.4, 'purchaseRate': 41.4},
                          {'baseCurrency': 'UAH', 'currency': 'GBP', 'saleRateNB': 44.4784, 'purchaseRateNB': 44.4784,
                           'saleRate': 48.2, 'purchaseRate': 44.27},
                          {'baseCurrency': 'UAH', 'currency': 'GEL', 'saleRateNB': 13.7948, 'purchaseRateNB': 13.7948},
                          {'baseCurrency': 'UAH', 'currency': 'HUF', 'saleRateNB': 0.102036,
                           'purchaseRateNB': 0.102036},
                          {'baseCurrency': 'UAH', 'currency': 'ILS', 'saleRateNB': 10.4856, 'purchaseRateNB': 10.4856},
                          {'baseCurrency': 'UAH', 'currency': 'JPY', 'saleRateNB': 0.27961, 'purchaseRateNB': 0.27961},
                          {'baseCurrency': 'UAH', 'currency': 'KZT', 'saleRateNB': 0.080877,
                           'purchaseRateNB': 0.080877},
                          {'baseCurrency': 'UAH', 'currency': 'MDL', 'saleRateNB': 1.9487, 'purchaseRateNB': 1.9487},
                          {'baseCurrency': 'UAH', 'currency': 'NOK', 'saleRateNB': 3.6092, 'purchaseRateNB': 3.6092},
                          {'baseCurrency': 'UAH', 'currency': 'PLN', 'saleRateNB': 8.3101, 'purchaseRateNB': 8.3101,
                           'saleRate': 8.9, 'purchaseRate': 8.17},
                          {'baseCurrency': 'UAH', 'currency': 'SEK', 'saleRateNB': 3.5312, 'purchaseRateNB': 3.5312},
                          {'baseCurrency': 'UAH', 'currency': 'SGD', 'saleRateNB': 27.6616, 'purchaseRateNB': 27.6616},
                          {'baseCurrency': 'UAH', 'currency': 'TMT', 'saleRateNB': 10.4482, 'purchaseRateNB': 10.4482},
                          {'baseCurrency': 'UAH', 'currency': 'TRY', 'saleRateNB': 1.9417, 'purchaseRateNB': 1.9417},
                          {'baseCurrency': 'UAH', 'currency': 'UAH', 'saleRateNB': 1.0, 'purchaseRateNB': 1.0},
                          {'baseCurrency': 'UAH', 'currency': 'USD', 'saleRateNB': 36.5686, 'purchaseRateNB': 36.5686,
                           'saleRate': 39.8, 'purchaseRate': 39.3},
                          {'baseCurrency': 'UAH', 'currency': 'UZS', 'saleRateNB': 0.0032448,
                           'purchaseRateNB': 0.0032448},
                          {'baseCurrency': 'UAH', 'currency': 'XAU', 'saleRateNB': 68822.11,
                           'purchaseRateNB': 68822.11}]}

    currency = ['EUR', 'USD']
    currency.extend(cur)
    result = ''
    result += d['date'] + '\n'
    for i in currency:
        for el in d['exchangeRate']:
            if i in el.values():
                result += f"{el['currency']} = Sale:{el.get('saleRate', el['saleRateNB'])} / Purchase:{el.get('purchaseRate', el['purchaseRateNB'])} \n"
                # print(el.get('saleRate', el['saleRateNB']))

    return f'{result}-----------------------------------'


print(represent(['SGD']))


#
# date = d['date']
# a = d['exchangeRate']
# for el in a:
#     if 'EUR' in el.values():
#         print(el)
# # print(z)