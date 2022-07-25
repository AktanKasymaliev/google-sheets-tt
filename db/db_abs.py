from abc import abstractmethod

from .configurations import get_config_data

from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table

class AbstractDB:

    def __init__(self) -> None:
        self.__set_config()
        self.engine = self.__create_connection()
        self.meta = MetaData()

    @abstractmethod
    def get_item(self) -> None:
        """ Method for getting items from db  """
        pass

    @abstractmethod
    def set_item(self) -> None:
        """ Method for setting items from db  """
        pass

    @abstractmethod
    def delete_item(self) -> None:
        """ Method for deleting items from db  """
        pass

    def create_table(self, 
            table_name: str, *columns) -> None:
        """
        > Create a table with the given name and columns, if it doesn't already exist
        
        :param table_name: The name of the table to create
        :type table_name: str
        """
        Table(
            table_name, 
            self.meta,
            keep_existing=True,
            *columns
        )
        self.meta.create_all(self.engine)

    def __create_connection(self):
        """
        It creates a connection to the database using the credentials provided in the constructor.
        :return: The engine object is being returned.
        """
        URL = f'postgresql://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}'
        engine = create_engine(URL)
        return engine
    
    def __set_config(self) -> None:
        """
        It reads the config file and sets the class variables to the values in the config file
        """
        self.password = get_config_data("DATABASE_PASSW")
        self.username = get_config_data("DATABASE_USER")
        self.host = get_config_data("DATABASE_HOST")
        self.port = get_config_data("DATABASE_PORT")
        self.database = get_config_data("DATABASE_NAME")