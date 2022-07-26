from .db_abs import AbstractDB
from .models import members

from sqlalchemy import text

class DB(AbstractDB):

    def __init__(self, database: str) -> None:
        super().__init__(database)
        self.__save_all_tables()

    def get_all_item(self, table_name: str) -> str:
        query = text(
                f"SELECT * FROM {table_name}"
                )
        return self.engine.execute(query).all()

    def set_item(self, table_name: str, columns: tuple, values: tuple) -> str:
        query = text(
            f"INSERT INTO {table_name} ({columns}) \
                VALUES ({values})"
        )
        item = self.engine.execute(query)
        return f"{item} added in {table_name}!"

    def __save_all_tables(self):
        """
        It creates a table for each class in the module, and the columns of the table are the attributes of
        the class.
        """
        tables = [member for member in members if not(member[0].startswith('__') and member[0].endswith('__'))]
        for table in tables:
            self.create_table(
                table[0].lower(),
                *table[1]
            )