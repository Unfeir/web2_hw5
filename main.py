import asyncio
import argparse
from datetime import date, timedelta

import logging

import aiohttp


parser = argparse.ArgumentParser(description='Currency')
parser.add_argument('--curr', '-c', required=True, default=['USD', 'EUR'], help='Choose currency')
parser.add_argument('--days', '-d', default=1, help='last _n_ days to show')
args = vars(parser.parse_args())
c = args.get('curr')
d = args.get('days')


def represent(request, cur=[]):
    currency = ['EUR', 'USD']
    currency.extend(cur)
    result = ''
    result += request['date'] + '\n'
    for i in currency:
        for el in request['exchangeRate']:
            if i in el.values():
                result += f"{el['currency']} = Sale:{el.get('saleRate', el['saleRateNB'])} / Purchase:{el.get('purchaseRate', el['purchaseRateNB'])} \n"
                # print(el.get('saleRate', el['saleRateNB']))

    return f'{result}-----------------------------------'


async def request(url):
    # print('request_f', url)
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as resp:
                logging.debug('request')
                if resp.status == 200:
                    txt = await resp.json()
                    return represent(txt)

                else:
                    logging.error(resp.status)
        except aiohttp.ClientConnectionError as err:
            logging.info({err})


def days_to_show(n):
    if n > 10:
        days = 10
    else:
        days = n

    return [date.today() - timedelta(days=n) for n in range(days)]


async def url_build(basicurl, days=1):
    days = days_to_show(days)

    for i in days:
        url = basicurl + i.strftime('%d.%m.%Y')
        yield request(url)


async def main(requests):
    result = []
    async for req in requests:
        result.append(req)
    return await asyncio.gather(*result)


if __name__ == '__main__':
    basic_url = 'https://api.privatbank.ua/p24api/exchange_rates?json&date='
    curr = ['EUR', 'USD']
    print(curr)
    print(d, c)
    # days_to = 3
    # logging.basicConfig(level=logging.DEBUG)
    # result = asyncio.run(main(url_build(basic_url, days_to)))
    # for i in result:
    #     print(i)

