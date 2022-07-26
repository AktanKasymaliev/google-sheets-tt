import inspect

from .models import SheetDBTables

sheet_members = inspect.getmembers(SheetDBTables, lambda a:not(inspect.isroutine(a)))