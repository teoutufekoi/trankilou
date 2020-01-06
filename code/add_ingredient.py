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
    
    # Generate a random GID
    gid = generate_gid()
    
    # Ask for the name of the ingredient
    name = click.prompt(click.style("Name?", fg="yellow", bold=True))
    
    # Ask for the unit using the list of existing units
    for i in range(len(units)):
        print("- " + str(i) + " - " + str(units[i].name))
    while True:
        action = click.prompt(click.style("Select a unit",
                                           fg="yellow", bold=True))
        if action.isdigit() and float(action) < len(units):
            unit = units[i].gid
            break
        else:
            click.secho("Please select a unit using a proper index.", fg="red", bold=True)
    
    # Ask for the domain using the list of existing domains
    for i in range(len(domains)):
        print("- " + str(i) + " - " + str(domains[i].name))
    while True:
        action = click.prompt(click.style("Select a domain",
                                          fg="yellow", bold=True))
        if action.isdigit() and float(action) < len(units):
            domain = domains[i].gid
            break
        else:
            click.secho("Please select a domain using a proper index.", fg="red", bold=True)
    
    # Create new ingredient
    ingredient = Ingredient(gid, name, domain, unit)

    # Add the ingredient to the list
    ingredients.append(ingredient)

    # List updated ingredient list
    list_ingredients()

    # Record the change to the JSON file
    record_ingredients()


def get_ingredient_input_key():
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
unit_path_data = sys.argv[1] + "units.json"
db_unit = JManager(unit_path_data)
units = db_unit.read_list(Unit.from_json)
domain_path_data = sys.argv[1] + "domains.json"
db_domain = JManager(domain_path_data)
domains = db_domain.read_list(Domain.from_json)

# Prompt input from user
get_ingredient_input_key()