from .db_abs import AbstractDB

from sqlalchemy import text

class DB(AbstractDB):

    def __init__(self, 
        password: str, dbname: str, 
        host: str, port: int, 
        user: str, tables_member: str) -> None:
        super().__init__(password, dbname, host, port, user)
        self.__save_all_tables(tables_member)

    def get_all_item(self, table_name: str) -> str:
        query = text(
                f"SELECT * FROM {table_name}"
                )
        return self.engine.execute(query).all()

    def delete_all_items(self, table_name) -> str:
        query = text(
                f"TRUNCATE TABLE {table_name}"
                )
        return self.engine.execute(query)

    def set_item(self, table_name: str, columns: str, values: str) -> str:
        query = text(
            f"INSERT INTO {table_name} ({columns}) \
                VALUES ({values})"
        )
        item = self.engine.execute(query)
        return f"{item} added in {table_name}!"

    def __save_all_tables(self, tables_member):
        """
        It creates a table for each class in the module, and the columns of the table are the attributes of
        the class.
        """
        tables = [member for member in tables_member if not(member[0].startswith('__') and member[0].endswith('__'))]
        for table in tables:
            self.create_table(
                table[0].lower(),
                *table[1]
            )