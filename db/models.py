from sqlalchemy import Column, Integer, String, Date

class SheetDBTables:
   Sheet = [
      Column('id', Integer, primary_key=True), 
      Column('number_of_order', String(255), unique=True), 
      Column('cost', Integer),
      Column('delivery_time', Date)
   ]
   Aktan = [
      Column('id', Integer, primary_key=True), 
      Column('number_of_order', String(255), unique=True), 
      Column('cost', Integer),
      Column('delivery_time', Date)
   ]