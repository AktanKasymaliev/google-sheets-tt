from datetime import datetime

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

def is_expired_date(date) -> bool:
    if datetime.now().date() > date:
        return True
    return False

def send_notification(orders: list) -> None:
    TOKEN = get_config_data("TG_TOKEN")
    CHAT_ID = get_config_data("CHAT_ID")
    message = f"""
*THESE ORDERS*: 
{orders} 
*HAS EXPIRED!*
    """
    URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}'
    requests.get(
        URL
    )

def make_date_for_comparing(order: dict) -> datetime.date:
    frmt = '%Y-%m-%d'
    return datetime.strptime(order[-1], frmt).date()