import datetime
import xmltodict

import requests

from db.db import DB
from configurations import get_config_data
from sheet.sheet import Sheet

def init_db(
    password: str, dbname: str, 
    host: str, port: int, 
    user: str, member) -> DB:
    return DB(
        password, dbname,
        host, port, 
        user, member
    )

def init_sheet(credentials: str, sheet_id: str, sheet_range: str) -> Sheet:
    return Sheet(
        credentials,
        sheet_id,
        sheet_range
        )

def get_dollar_currency(date) -> float:
    URL = f"http://www.cbr.ru/scripts/XML_daily.asp?date_req={date}"
    response = requests.get(URL)
    rub_to_dollar = parse_xml_data(response)

    return rub_to_dollar


def parse_xml_data(response) -> float:
    xml_data = xmltodict.parse(response.content)

    for order in xml_data['ValCurs']['Valute']:
        if order['@ID'] == 'R01235':
            rub = float(order['Value'].replace(',', '.'))

    return rub

def is_expired_date(date) -> bool:
    if datetime.datetime.now().date() > date:
        return True
    return False

def send_notification(orders: list) -> None:
    TOKEN = get_config_data("TG_TOKEN")
    CHAT_ID = get_config_data("CHAT_ID")
    message = f"""
THESE ORDERS: '{orders}' has expired!
    """
    URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}'
    requests.get(
        URL
    )