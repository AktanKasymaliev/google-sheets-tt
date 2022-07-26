from datetime import datetime

from db.db import DB
from sheet.sheet import Sheet

from sqlalchemy.exc import IntegrityError

class Worker:
    
    def __init__(self, db: DB, sheet: Sheet) -> None:
        self.db = db
        self.sheet = sheet
        self.data = self.sheet.read_sheet()['values']

    def parse_sheet_data(self) -> list:
        parsed_data = []
        for index in range(len(self.data[0])):
            parsed_data.append([
                self.__return_divided_data(
                    self.data, 
                    count, 
                    index)
                    for count in range(len(self.data))
                ])
        parsed_data.pop(0)
        return parsed_data
    
    def save_data_to_database(self):
        parsed_records = self.parse_sheet_data()
        try:
            for record in parsed_records:
                # Formating from your datestamp to database's
                formated_date = datetime.strptime(record[-1], '%d.%m.%Y')
                record[-1] = formated_date.strftime('%Y-%m-%d')
                self.db.set_item(
                        "sheet",
                        "id, number_of_order, cost, delivery_time",
                        "{}, '{}', {}, '{}'".format(*record)
                    )
        except IntegrityError:
            print("\nSome Google Sheet records are alredy in database!\nIf the sheet had new records - they were added to database\n")

    def get_all_records_from_db(self):
        return self.db.get_all_item('sheet')

    @staticmethod
    def __return_divided_data(
        data: list, first_index: int, 
        second_index: int
        ) -> None:

        return data[first_index][second_index]