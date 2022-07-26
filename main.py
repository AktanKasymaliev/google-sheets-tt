from db import sheet_members
from db.db import DB
from db.configurations import config, get_config_data
from sheet.sheet import Sheet

def main():
    config()

    sheet_range = 'A1:D60'
    data = Sheet(
        'creds.json',
        '1Y9pLQIA8D0FuoyY5UM3Syqi5jyw-s3bqRHnLFyGnrPg'
        ).read_sheet(sheet_range)

    db = DB(
        get_config_data("DATABASE_NAME"),
        sheet_members
        )
    return

if __name__ == "__main__":
    main()