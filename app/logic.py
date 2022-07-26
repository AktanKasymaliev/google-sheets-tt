from db.db import DB
from sheet.sheet import Sheet

class Worker:
    
    def __init__(self, db: DB, sheet: Sheet) -> None:
        self.db = db
        self.sheet = sheet

    def parse_sheet_data(self):
        print(self.sheet.read_sheet())