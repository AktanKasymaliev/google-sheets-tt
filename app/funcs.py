import xmltodict
import requests

from db.db import DB
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

    for currency in xml_data['ValCurs']['Valute']:
        if currency['@ID'] == 'R01235':
            rub = float(currency['Value'].replace(',', '.'))

    return rub