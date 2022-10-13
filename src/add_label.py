import click
import binascii
import os
from cookbook import *
from database import *


def generate_gid():
    nbytes = 4
    random_bytes = os.urandom(nbytes)
    return binascii.hexlify(random_bytes).decode('ascii')


def list_labels():
    print('\n'.join(str(i.name) for i in labels))


def record_labels():
    db.record_list(labels)


def add_label():
    # Get information from the user
    name = click.prompt(click.style("Name?", fg="yellow", bold=True))
    gid = generate_gid()

    # Create new label
    label = Label(gid, name)

    # Add the ingredient to the list
    labels.append(label)

    # List updated ingredient list
    list_labels()

    # Record the change to the JSON file
    record_labels()


def get_input_key():
    info = ""
    info += "'l' => list the current labels\n"
    info += "'a' => add new label\n"
    info += "'q' => record and quit\n"
    click.secho(info, fg="yellow", bold=True)
    while True:
        action = click.prompt(click.style("Select an action",
                                           fg="yellow", bold=True))
        if action == "l":
            list_labels()
        elif action == "a":
            add_label()
        elif action == "q":
            print("Ciao!!")
            exit(0)
        else:
            click.secho("Invalid choice", fg="red", bold=True)
    return confkey


if __name__ == "__main__":
    import sys

# Initialize the list of labels from the JSON file
data_path = sys.argv[1] + "labels.json"
db = JManager(data_path)
labels = db.read_list(Label.from_json)

# Prompt input from user
get_input_key()