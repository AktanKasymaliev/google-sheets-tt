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