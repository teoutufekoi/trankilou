import click
import binascii
import os
from cookbook import *
from database import *


'''
Iterate over all the key value pairs in dictionary and call the given
callback function() on each pair. Items for which callback() returns True,
add them to the new dictionary. In the end return the new dictionary.
'''
def filterTheDict(dictObj, callback):
    newDict = dict()
    # Iterate over all the items in dictionary
    for (key, value) in dictObj.items():
        # Check if item satisfies the given condition then add to new dict
        if callback((key, value)):
            newDict[key] = value
    return newDict


def generate_gid():
    nbytes = 4
    random_bytes = os.urandom(nbytes)
    return binascii.hexlify(random_bytes).decode('ascii')


def list_recipes(recipes):
    print('\n'.join(str(i.name) for i in recipes))


def get_recipe(key, recipes_list):
    recipe = next((item for item in recipes_list if item.gid == key), None)
    return recipe


def get_ingredient(key, ingredients_list):
    ingredient = next((item for item in ingredients_list if item.gid == key), None)
    return ingredient


def get_domain(key, domains_list):
    domain = next((item for item in domains_list if item.gid == key), None)
    return domain


def get_unit(key, unit_list):
    unit = next((item for item in unit_list if item.gid == key), None)
    if unit is None:
        return "n/a"
    else:
        return unit.short


