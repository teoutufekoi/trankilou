import os
from Google import Create_Service

FOLDER_PATH = r'.'
CLIENT_SECRET_FILE = os.path.join(FOLDER_PATH, 'credentials-trankilou.json')

API_SERVICE_NAME = 'sheets'
API_VERSION = 'v4'

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

service = Create_Service(CLIENT_SECRET_FILE, API_SERVICE_NAME, API_VERSION, SCOPES)

# """
# Blank Spreadsheet file
# """
# sheets_file1 = service.spreadsheets().create().execute()
# print(sheets_file1)
# print(sheets_file1['spreadsheetUrl'])
#
# """
# Advanced Example: Spreadsheets File with some default settings
# """
# sheet_body = {
#     'properties': {
#         'title': 'Trankilou data'
#     },
#     'sheets': [
#         {
#             'properties': {
#                 'title': 'First'
#             }
#         },
#         {
#             'properties': {
#                 'title': 'Second'
#             }
#         },
#         {
#             'properties': {
#                 'title': 'Third'
#             }
#         }
#     ]
# }
# sheets_file2 = service.spreadsheets().create(
#     body=sheet_body
# ).execute()
#
# print(sheets_file2)
# print(sheets_file2['spreadsheetUrl'])

spreadsheet_id = '19CMu93WS4iXYofPqS8CDEvxUuDk4OuoEfLqkkHroZDY'
mySpreadsheets = service.spreadsheets().get(spreadsheetId=spreadsheet_id).execute()


"""
values.update
"""

worksheet_name = 'recipes!'
cell_range_insert = 'B2'
values = (
    ('Col A', 'Col B', 'Col C'),
    ('Apple', 'Orange', 'Watermelon')
)

value_range_body = {
    'majorDimension': 'ROWS',
    'values': values
}

service.spreadsheets().values().update(
    spreadsheetId=spreadsheet_id,
    valueInputOption='USER_ENTERED',
    range=worksheet_name + cell_range_insert,
    body=value_range_body
).execute()

service.spreadsheets().values().clear(
    spreadsheetId=spreadsheet_id,
    range='recipes'
).execute()

worksheet_name = 'recipes!'
cell_range_insert = 'B2'
values = (
    ('Col A', 'Col B', 'Col C'),
    ('Apple', 'Orange', 'Watermelon')
)

value_range_body = {
    'majorDimension': 'COLUMNS',
    'values': values
}

service.spreadsheets().values().update(
    spreadsheetId=spreadsheet_id,
    valueInputOption='USER_ENTERED',
    range=worksheet_name + cell_range_insert,
    body=value_range_body
).execute()


"""
values.append
"""

worksheet_name = 'recipes!'
cell_range_insert = 'B2'
values = (
    ('Col D', 'Col E', 'Col F'),
    ('Toyota', 'Honda', 'Testla')
)

value_range_body = {
    'majorDimension': 'COLUMNS',
    'values': values
}

service.spreadsheets().values().append(
    spreadsheetId=spreadsheet_id,
    valueInputOption='USER_ENTERED',
    range=worksheet_name + cell_range_insert,
    body=value_range_body
).execute()

