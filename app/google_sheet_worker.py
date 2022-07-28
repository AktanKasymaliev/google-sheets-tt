import asyncio

from db.db import DB
from sheet.sheet import Sheet
from .async_funcs import init_async_funcs

from sqlalchemy.exc import IntegrityError

class GoogleSheetWorker:
    
    def __init__(self, db: DB, sheet: Sheet) -> None:
        self.db = db
        self.sheet_table = "sheet"
        self.sheet = sheet
        self.data = self.sheet.read_sheet()['values']

    def parse_sheet_data(self) -> list:
        """
        It takes the data from the sheet, and then it divides it into a list of lists, 
        where each list is a column of data.

        :return: A list of lists.
        """
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
        """
        It takes the data from the Google Sheet, and saves it to the database
        """
        self.db.delete_all_items(self.sheet_table)

        parsed_order = self.parse_sheet_data()
        ready_orders = asyncio.run(init_async_funcs(parsed_order))
        
        for order in ready_orders: 
            try:
                self.db.set_item(
                        self.sheet_table,
                        "id, number_of_order, cost, delivery_time",
                        "{}, '{}', {}, '{}'".format(*order)
                    )
            except IntegrityError:
                continue

    def get_all_records_from_db(self) -> list:
        return self.db.get_all_item(self.sheet_table)

    @staticmethod
    def __return_divided_data(
        data: list, first_index: int, 
        second_index: int
        ) -> None:
        """
        > This function returns the data at the specified index
        
        :param data: list = The data that you want to divide
        :type data: list
        :param first_index: The index of the first list in the list of lists
        :type first_index: int
        :param second_index: The index of the data you want to return
        :type second_index: int
        :return: The data is being returned.
        """

        return data[first_index][second_index]