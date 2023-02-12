import asyncio
import logging
from datetime import date, timedelta
import re

import aiohttp
import websockets
import names
from websockets import WebSocketServerProtocol
from websockets.exceptions import ConnectionClosedOK

logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s, %(levelname)s - %(message)s')

stream = logging.StreamHandler()
stream.setLevel(logging.INFO)
stream.setFormatter(formatter)
logger.addHandler(stream)

file = logging.FileHandler('logs.log')
file.setLevel(logging.CRITICAL)
file.setFormatter(formatter)
logger.addHandler(file)

logging.basicConfig(level=logging.INFO, handlers=[logging.FileHandler('logs.log'), logging.StreamHandler()])


async def request(url):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    return data
                logging.error(f"Error status {response.status} for {url}")
        except aiohttp.ClientConnectorError as e:
            logging.error(f"Connection error {url}: {e}")
        return None


def days_to_show(n):
    if int(n) > 10:
        days = 10
    else:
        days = int(n)

    return [date.today() - timedelta(days=n) for n in range(days)]


async def url_build(days):
    basicurl = 'https://api.privatbank.ua/p24api/exchange_rates?json&date='
    return [basicurl + day.strftime('%d.%m.%Y') for day in days_to_show(days)]


async def get_exchange(urls, curr):
    result = []

    for url in urls:
        res = await request(url)
        for el in res['exchangeRate']:
            if curr in el.values():
                result.append(
                    f"{res['date']}: {el['currency']} = Sale:{el.get('saleRate', el['saleRateNB'])} / Purchase:{el.get('purchaseRate', el['purchaseRateNB'])}")

    return result


async def parser(data):
    days = re.search(r'\d+', data)
    cur = re.search(r'[a-zA-Z]+', data)
    args = {'days': 1, 'cur': 'USD'}
    if days:
        args['days'] = days.group()
    if cur:
        args['cur'] = cur.group()
    return args


class Server:
    clients = set()

    async def register(self, ws: WebSocketServerProtocol):
        ws.name = names.get_full_name()
        self.clients.add(ws)
        logging.info(f'{ws.remote_address} connects')

    async def unregister(self, ws: WebSocketServerProtocol):
        self.clients.remove(ws)
        logging.info(f'{ws.remote_address} disconnects')

    async def send_to_clients(self, message: str):
        if self.clients:
            [await client.send(message) for client in self.clients]

    async def send_to_client(self, message: str, ws: WebSocketServerProtocol):
        await ws.send(message)

    async def ws_handler(self, ws: WebSocketServerProtocol):
        await self.register(ws)
        try:
            await self.distrubute(ws)
        except ConnectionClosedOK:
            pass
        finally:
            await self.unregister(ws)

    async def distrubute(self, ws: WebSocketServerProtocol):
        async for message in ws:
            if message.startswith('exchange'):
                logging.critical(f'{ws.name} - request exchange')
                args = await parser(message.removeprefix('exchange').lstrip().upper())
                r = await get_exchange(await url_build(args['days']), args['cur'])
                for i in r:
                    await self.send_to_client(i, ws)
            else:
                await self.send_to_clients(f"{ws.name}: {message}")


async def main():
    server = Server()
    async with websockets.serve(server.ws_handler, 'localhost', 8080):
        await asyncio.Future()  # run forever


if __name__ == '__main__':
    asyncio.run(main())
