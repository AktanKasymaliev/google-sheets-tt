from db.db import DB
from sheet.sheet import Sheet

def init_db(database_name: str, member) -> DB:
    return DB(
        database_name,
        member
    )

def init_sheet(credentials: str, sheet_id: str, sheet_range: str) -> Sheet:
    return Sheet(
        credentials,
        sheet_id,
        sheet_range
        )