from sheet.sheet import Sheet
from db.configurations import config 
from db.db import DB

def main():
    config()

    sheet_range = 'A1:D60'
    data = Sheet(
        'creds.json',
        '1Y9pLQIA8D0FuoyY5UM3Syqi5jyw-s3bqRHnLFyGnrPg'
        ).read_sheet(sheet_range)

    db = DB()
    
    return data

if __name__ == "__main__":
    main()