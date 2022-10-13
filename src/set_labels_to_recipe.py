import click
import binascii
import os
from cookbook import *
from database import *


def list_recipes():
    for i in range(len(recipes)):
        print("- " + str(i) + " - " + str(recipes[i].name))


def record_recipes():
    db.record_list(recipes)


def set_labels_for_recipe(recipe_index):

    # Select the labels
    while True:

        # Print recipe name
        print("Recipe = " + recipes[recipe_index].name + " (" + str(recipe_index) + ")")
        print("Recipe date = " + recipes[recipe_index].date + " (" + str(recipe_index) + ")")
        print("Recipe author = " + recipes[recipe_index].author + " (" + str(recipe_index) + ")")

        # Ask for the label using the list of existing labels
        for i in range(len(all_labels)):
            # Get to know if the label is currently associated with the recipe
            marker = "*" if all_labels[i].gid in recipes[recipe_index].labels else " "

            # Print the label accordingly
            print(marker + " " + str(all_labels[i].name) + " (" + str(i) + ") ")

        # Capture the selection
        action = click.prompt(click.style("Select one or several labels using coma for separation. Press 'q' to quit.",
                                          fg="yellow", bold=True))

        # Make sure we can quit the label selection
        if action == "q":
            break

        for raw_label_number in action.split(","):
            label_number = raw_label_number.strip()
            if not label_number.isdigit() or float(label_number) >= len(all_labels):
                click.secho("Please select labels using proper indices separated by a coma.", fg="red", bold=True)
                break
            label_gid = all_labels[int(label_number)].gid

            # Add the label to the recipe
            recipes[recipe_index].add_label(label_gid)


def get_recipe_input_key():
    info = ""
    info += "select the id for a given recipe\n"
    info += "'q' => record and quit\n"
    click.secho(info, fg="yellow", bold=True)
    while True:
        list_recipes()

        action = click.prompt(click.style("Which recipe do you want to edit? ('q' to quit)",
                                          fg="yellow", bold=True))
        if action.isdigit() and float(action) < len(recipes):

            # Set the labels
            recipe_index = int(action)
            set_labels_for_recipe(recipe_index)

            # Record the changes
            record_recipes()

        elif action == "q":
            print("Ciao!!")
            exit(0)
        else:
            click.secho("Please select a recipe using a proper index.", fg="red", bold=True)
    return confkey


if __name__ == "__main__":
    import sys

# Initialize the list of recipes from the JSON file
data_path = sys.argv[1] + "recipes.json"
db = JManager(data_path)
recipes = db.read_list(Recipe.from_json)
labels_path_data = sys.argv[1] + "labels.json"
db_labels = JManager(labels_path_data)
all_labels = db_labels.read_list(Label.from_json)

# Prompt input from user
get_recipe_input_key()