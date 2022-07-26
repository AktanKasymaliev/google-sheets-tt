import inspect

from sqlalchemy import Column, Integer, String, Date

class Tables:
   Sheet = [
      Column('id', Integer, primary_key=True), 
      Column('number_of_order', String(255), unique=True), 
      Column('cost', Integer),
      Column('delivery_time', Date)
   ]

members = inspect.getmembers(Tables, lambda a:not(inspect.isroutine(a)))
