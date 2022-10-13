import click
import binascii
import os
from cookbook import *
from database import *


def generate_gid():
    nbytes = 4
    random_bytes = os.urandom(nbytes)
    return binascii.hexlify(random_bytes).decode('ascii')


def list_units():
    print('\n'.join(str(i.name) + " - " + str(i.short) for i in units))


def record_units():
    db.record_list(units)


def add_unit():
    # Get information from the user
    name = click.prompt(click.style("Name?", fg="yellow", bold=True))
    short = click.prompt(click.style("Short name?", fg="yellow", bold=True))
    gid = generate_gid()

    # Create new ingredient
    unit = Unit(gid, name, short)

    # Add the ingredient to the list
    units.append(unit)

    # List updated ingredient list
    list_units()

    # Record the change to the JSON file
    record_units()


def get_input_key():
    info = ""
    info += "'l' => list the current units\n"
    info += "'a' => add new units\n"
    info += "'q' => record and quit\n"
    click.secho(info, fg="yellow", bold=True)
    while True:
        action = click.prompt(click.style("Select an action",
                                           fg="yellow", bold=True))
        if action == "l":
            list_units()
        elif action == "a":
            add_unit()
        elif action == "q":
            print("Ciao!!")
            exit(0)
        else:
            click.secho("Invalid choice", fg="red", bold=True)
    return confkey


if __name__ == "__main__":
    import sys

# Initialize the list of ingredients from the JSON file
data_path = sys.argv[1] + "units.json"
db = JManager(data_path)
units = db.read_list(Unit.from_json)

# Prompt input from user
get_input_key()