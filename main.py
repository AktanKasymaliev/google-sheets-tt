from sheet.sheet import Sheet

def main():
    data = Sheet('creds.json').read_sheet('A1:D60')
    return data

if __name__ == "__main__":
    main()