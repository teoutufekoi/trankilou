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
Insert new tasklist
"""
# tasklistShoppingList = service.tasklists().insert(
#     body={'title': '02 Oct 2020 - Shopping list'}
# ).execute()

tasklistId = 'RWtNLVNoYTVZSFFkbi1SRA'


"""
Insert couples of ingredients
"""


def construct_request_body(title, notes=None, due=None, status='needsAction', deleted=False):
    try:
        request_body = {
            'title': title,
            'notes': notes,
            'due': due,
            'deleted': deleted,
            'status': status
        }
        return request_body
    except Exception:
        return None


ingredients = {
        'fruits et légumes': [
            {
                'name': 'pommes de terre',
                'quantity': '5kg'
            },
            {
                'name': 'oignons',
                'quantity': '3pc'
            }
        ],
        'produits frais': [
            {
                'name': 'beurre',
                'quantity': '250g'
            },
            {
                'name': 'crème fraîche',
                'quantity': '50cl'
            }
        ],
}

previousDomainId = None
for domain in ingredients:
    request_body = construct_request_body(
        title=domain
    )
    response = service.tasks().insert(
        tasklist=tasklistId,
        body=request_body,
        previous=previousDomainId
    ).execute()
    previousDomainId = response.get('id')

    previousIngredientId = None
    for ingredient in ingredients[domain]:
        request_body = construct_request_body(
            title=ingredient['name'],
            notes=ingredient['quantity']
        )
        response = service.tasks().insert(
            tasklist=tasklistId,
            body=request_body,
            previous=previousIngredientId,
            parent=previousDomainId
        ).execute()
        previousIngredientId = response.get('id')

