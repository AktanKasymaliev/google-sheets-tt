# API = "AIzaSyA7D4AGAFcyUP88PxKyLz3c1ZQzyRNQxJA"

from pprint import pprint

import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials


# Файл, полученный в Google Developer Console
CREDENTIALS_FILE = 'creds.json'
# ID Google Sheets документа
SPREASHEET_ID = '1Y9pLQIA8D0FuoyY5UM3Syqi5jyw-s3bqRHnLFyGnrPg'

# Авторизуемся и получаем service — экземпляр доступа к API
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)

# Пример чтения файла
values = service.spreadsheets().values().get(
    spreadsheetId=SPREASHEET_ID,
    range='A1:E10',
    majorDimension='COLUMNS'
).execute()
pprint(values)
exit()