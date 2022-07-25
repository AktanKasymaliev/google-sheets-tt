from abc import abstractmethod

import httplib2

class AbstractSheet:
    # ID Google Sheets документа
    _SPREASHEET_ID = '1Y9pLQIA8D0FuoyY5UM3Syqi5jyw-s3bqRHnLFyGnrPg'
    _SCOPES = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
        ]

    def __init__(self, creds_filename: str) -> None:
        self.creds_filename = creds_filename

    @abstractmethod
    def __login_and_build_sheet(self) -> httplib2.Http:
        pass
    
    @abstractmethod
    def read_sheet(self, range: str) -> dict:
        pass