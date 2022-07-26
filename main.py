from pprint import pprint

from db import sheet_members
from db.configurations import config, get_config_data
from app.workers import GoogleSheetWorker
from app.funcs import init_db, init_sheet

def main():
    config()
    
    sheet_range = 'A1:D60'
    credentials = 'creds.json'
    sheet_id = '1Y9pLQIA8D0FuoyY5UM3Syqi5jyw-s3bqRHnLFyGnrPg'

    sheet_db = init_db(
        password=get_config_data("DATABASE_PASSW"),
        user=get_config_data("DATABASE_USER"),
        host=get_config_data("DATABASE_HOST"),
        port=int(get_config_data("DATABASE_PORT")),
        dbname=get_config_data("DATABASE_NAME"),
        
        member=sheet_members)
    sheet = init_sheet(credentials, sheet_id, sheet_range)

    w = GoogleSheetWorker(sheet_db, sheet)
    w.save_data_to_database()
    pprint(w.get_all_records_from_db())

if __name__ == "__main__":
    main()