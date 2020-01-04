import click
import binascii
import os
from cookbook import *
from database import *


def generate_gid():
    nbytes = 4
    random_bytes = os.urandom(nbytes)
    return binascii.hexlify(random_bytes).decode('ascii')


def list_ingredients():
    print('\n'.join(str(i.domain) + " - " + str(i.name) + " (" + str(i.unit) + ")" for i in ingredients))


def record_ingredients():
    db.record_list(ingredients)


def add_ingredient():
    # Get information from the user
    name = click.prompt(click.style("Name?", fg="yellow", bold=True))
    domain = click.prompt(click.style("Domain?", fg="yellow", bold=True))
    unit = click.prompt(click.style("Unit?", fg="yellow", bold=True))
    gid = generate_gid()

    # Create new ingredient
    ingredient = Ingredient(gid, name, domain, unit)

    # Add the ingredient to the list
    ingredients.append(ingredient)

    # List updated ingredient list
    list_ingredients()

    # Record the change to the JSON file
    record_ingredients()


def get_input_key():
    info = ""
    info += "'l' => list the current ingredients\n"
    info += "'a' => add new ingredient\n"
    info += "'q' => record and quit\n"
    click.secho(info, fg="yellow", bold=True)
    while True:
        action = click.prompt(click.style("Select an action",
                                           fg="yellow", bold=True))
        if action == "l":
            list_ingredients()
        elif action == "a":
            add_ingredient()
        elif action == "q":
            print("Ciao!!")
            exit(0)
        else:
            click.secho("Invalid choice", fg="red", bold=True)
    return confkey


if __name__ == "__main__":
    import sys

# Initialize the list of ingredients from the JSON file
data_path = sys.argv[1] + "ingredients.json"
db = JManager(data_path)
ingredients = db.read_list(Ingredient.from_json)

# Prompt input from user
get_input_key()