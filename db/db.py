from .db_abs import AbstractDB
from .models import members

class DB(AbstractDB):

    def __init__(self) -> None:
        super().__init__()
        self.__save_all_tables()
        

    def get_item(self) -> None:
        "TODO"
        return super().get_item()

    def set_item(self) -> None:
        "TODO"
        return super().set_item()
    
    def delete_item(self) -> None:
        "TODO"
        return super().delete_item()
        
    def __save_all_tables(self):
        tables = [member for member in members if not(member[0].startswith('__') and member[0].endswith('__'))]
        for table in tables:
            self.create_table(
                table[0].lower(),
                *table[1]
            )