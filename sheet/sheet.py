from .sheet_abs import AbstractSheet

import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials

class Sheet(AbstractSheet):

    def __init__(self, creds_filename: str) -> None:
        super().__init__(creds_filename)
        self._service = self.__login_and_build_sheet()

    def __login_and_build_sheet(self) -> httplib2.Http:
        # Log in and get service — instance to API
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
                        self.creds_filename, 
                        self._SCOPES
                        )
        http_auth = credentials.authorize(httplib2.Http())

        return apiclient.discovery.build('sheets', 'v4', http=http_auth)

    def read_sheet(self, range: str) -> dict:
        return self._service.spreadsheets().values().get(
        spreadsheetId=self._SPREASHEET_ID,
        range=range,
        majorDimension='COLUMNS'
    ).execute()