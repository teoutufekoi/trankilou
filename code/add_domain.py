import click
import binascii
import os
from cookbook import *
from database import *


def generate_gid():
    nbytes = 4
    random_bytes = os.urandom(nbytes)
    return binascii.hexlify(random_bytes).decode('ascii')


def list_domains():
    print('\n'.join(str(i.name) for i in domains))


def record_domains():
    db.record_list(domains)


def add_domain():
    # Get information from the user
    name = click.prompt(click.style("Name?", fg="yellow", bold=True))
    gid = generate_gid()

    # Create new ingredient
    domain = domain(gid, name)

    # Add the ingredient to the list
    domains.append(domain)

    # List updated ingredient list
    list_domains()

    # Record the change to the JSON file
    record_domains()


def get_input_key():
    info = ""
    info += "'l' => list the current domains\n"
    info += "'a' => add new domains\n"
    info += "'q' => record and quit\n"
    click.secho(info, fg="yellow", bold=True)
    while True:
        action = click.prompt(click.style("Select an action",
                                           fg="yellow", bold=True))
        if action == "l":
            list_domains()
        elif action == "a":
            add_domain()
        elif action == "q":
            print("Ciao!!")
            exit(0)
        else:
            click.secho("Invalid choice", fg="red", bold=True)
    return confkey


if __name__ == "__main__":
    import sys

# Initialize the list of ingredients from the JSON file
data_path = sys.argv[1] + "domains.json"
db = JManager(data_path)
domains = db.read_list(domain.from_json)

# Prompt input from user
get_input_key()