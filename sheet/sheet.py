from .sheet_abs import AbstractSheet

import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials

class Sheet(AbstractSheet):

    def __init__(self, creds_filename: str, sheet_id: str) -> None:
        super().__init__(creds_filename, sheet_id)
        self._service = self.__login_and_build_sheet()

    def __login_and_build_sheet(self) -> httplib2.Http:
        """
        > Log in to Google Sheets API and return a service instance to the API
        """
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
                        self.creds_filename, 
                        self._SCOPES
                        )
        http_auth = credentials.authorize(httplib2.Http())

        return apiclient.discovery.build('sheets', 'v4', http=http_auth)

    def read_sheet(self, range: str) -> dict:
        """
        > This function reads the data from the Google Sheet and returns it as a dictionary
        
        :param range: The range of cells to read
        :type range: str
        :return: A dictionary with the values of the spreadsheet.
        """
        return self._service.spreadsheets().values().get(
        spreadsheetId=self._SPREASHEET_ID,
        range=range,
        majorDimension='COLUMNS'
    ).execute()