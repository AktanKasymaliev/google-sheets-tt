import asyncio
from datetime import datetime
import xmltodict

import aiohttp

from .funcs import is_expired_date
from .funcs import send_notification
from .funcs import make_date_for_comparing

async def make_ready_to_save_to_db(order: list, date) -> list:
    URL = f"http://www.cbr.ru/scripts/XML_daily.asp?date_req={date}"

    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as response:
            rub_to_dollar = await parse_xml_data(await response.text())
            order[2] = round(int(order[2]) * rub_to_dollar, 2)
    return order


async def parse_xml_data(response) -> float:
    xml_data = xmltodict.parse(response)

    for order in xml_data['ValCurs']['Valute']:
        if order['@ID'] == 'R01235':
            rub = float(order['Value'].replace(',', '.'))

    return rub

async def convert_date(record_date: str, from_: str, to: str) -> str:
    """
    > This function takes a date string, converts it to a datetime object, and then returns a string in
    the format specified by the user
    """
    formated_date = datetime.strptime(record_date, from_)
    return formated_date.strftime(to)

async def init_async_funcs(orders: list):
    tasks = []
    expired_orders = []
    for order in orders:
        order[-1] = await convert_date(order[-1], '%d.%m.%Y', '%Y-%m-%d')

        if is_expired_date(make_date_for_comparing(order)):
            expired_orders.append(int(order[1]))

        task = asyncio.create_task(make_ready_to_save_to_db(
            order,
            await convert_date(
                    record_date=order[-1],
                    from_='%Y-%m-%d',
                    to='%d/%m/%Y'
                    ),
                )
            )
        tasks.append(task)
    ready_orders = await asyncio.gather(*tasks)
    send_notification(expired_orders)
    return ready_orders