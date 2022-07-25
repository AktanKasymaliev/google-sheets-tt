from abc import abstractmethod

import httplib2

class AbstractSheet:
    # ID Google Sheets документа
    _SCOPES = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
        ]

    def __init__(self, creds_filename: str, sheet_id: str) -> None:
        self.creds_filename = creds_filename
        self.sheet_id = sheet_id

    @abstractmethod
    def __login_and_build_sheet(self) -> httplib2.Http:
        pass
    
    @abstractmethod
    def read_sheet(self, range: str) -> dict:
        pass