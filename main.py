from db import sheet_members
from db.configurations import config, get_config_data
from app.logic import Worker
from app.funcs import init_db, init_sheet

def main():
    config()
    sheet_range = 'A1:D60'
    credentials = 'creds.json'
    sheet_id = '1Y9pLQIA8D0FuoyY5UM3Syqi5jyw-s3bqRHnLFyGnrPg'

    db = init_db(get_config_data("DATABASE_NAME"), sheet_members)
    sheet = init_sheet(credentials, sheet_id, sheet_range)

    w = Worker(db, sheet).parse_sheet_data()
    
    return

if __name__ == "__main__":
    main()