import pandas as pd
import os
from Google import Create_Service

FOLDER_PATH = r'.'
CLIENT_SECRET_FILE = os.path.join(FOLDER_PATH, 'credentials-trankilou.json')

API_SERVICE_NAME = 'tasks'
API_VERSION = 'v1'

SCOPES = ['https://www.googleapis.com/auth/tasks']

service = Create_Service(CLIENT_SECRET_FILE, API_SERVICE_NAME, API_VERSION, SCOPES)

"""
Insert method
"""
tasklistShoppingList = service.tasklists().insert(
    body={'title': '01 Oct 2020 - Shopping list - Premier essai'}
).execute()


"""
List method
"""
response = service.tasklists().list().execute()
lstItems = response.get('items')
nextPageToken = response.get('nextPageToken')

while nextPageToken:
    response = service.tasklists().list(
        maxResults=30,
        pageToken=nextPageToken
    ).execute()
    lstItems.extend(response.get('items'))
    nextPageToken = response.get('nextPageToken')

print(pd.DataFrame(lstItems).head())

pd.set_option('display.max_columns', 100)
pd.set_option('display.max_rows', 500)
pd.set_option('display.min_rows', 500)
pd.set_option('display.max_colwidth', 150)
pd.set_option('display.width', 120)
pd.set_option('expand_frame_repr', True)

"""
Delete Method
"""
for item in lstItems:
    try:
        if isinstance(int(item.get('title').replace('Tasklist #', '')), int):
            if int(item.get('title').replace('Tasklist #', '')) > 0:
                # print(int(item.get('title').replace('Tasklist #', '')))
                service.tasklists().delete(tasklist=item.get('id')).execute()
    except:
        pass

response = service.tasklists().list(maxResults=100).execute()
print(pd.DataFrame(response.get('items')))

"""
Update Method
"""
mainTasklist = response.get('items')[1]
mainTasklist['title'] = 'Restaurants to eat'
service.tasklists().update(tasklist=mainTasklist['id'], body=mainTasklist).execute()

"""
Get Method
"""
print(service.tasklists().get(tasklist='dnljMmxKWDJ0ZTBYcWdZZg').execute())

