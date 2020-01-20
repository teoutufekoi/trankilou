import click
import binascii
import os
from cookbook import *
from database import *


def generate_gid():
    nbytes = 4
    random_bytes = os.urandom(nbytes)
    return binascii.hexlify(random_bytes).decode('ascii')


def list_recipes(recipes):
    print('\n'.join(str(i.name) for i in recipes))


def get_recipe(key, recipes_list):
    recipe = next((item for item in recipes_list if item.gid == key), None)
    return recipe


def get_unit(key, unit_list):
    unit = next((item for item in all_units if item.gid == key), None)
    if unit is None:
        return "n/a"
    else:
        return unit.short


