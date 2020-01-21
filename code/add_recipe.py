import click
import binascii
import os
from cookbook import *
from database import *


def generate_gid():
    nbytes = 4
    random_bytes = os.urandom(nbytes)
    return binascii.hexlify(random_bytes).decode('ascii')


def list_recipes():
    print('\n'.join(str(i.name) for i in recipes))


def record_recipes():
    db.record_list(recipes)


def get_unit(key):
    unit = next((item for item in all_units if item.gid == key), None)
    if unit is None:
        return "n/a"
    else:
        return unit.short


def add_ingredient(ingredients):
    # Initiate the ingredient structure
    ingredient = {}

    # Ask for the ingredient using the list of existing ingredients
    for i in range(len(all_ingredients)):
        print("- " + str(i) + " - " + str(all_ingredients[i].name) + " (" + get_unit(str(all_ingredients[i].unit)) + ")")

    # Select the ingredient
    while True:
        action = click.prompt(click.style("Select an ingredient",
                                          fg="yellow", bold=True))
        if action.isdigit() and float(action) < len(all_ingredients):
            ingredient["gid"] = all_ingredients[int(action)].gid
            break
        else:
            click.secho("Please select an ingredient using a proper index.", fg="red", bold=True)

    # Select the quantity
    while True:
        action = click.prompt(click.style("Select the quantity",
                                          fg="yellow", bold=True))
        try:
            ingredient["quantity"] = float(action)
            break
        except ValueError:
            click.secho("Please enter a number.", fg="red", bold=True)

    # Add the ingredient to the list
    ingredients.append(ingredient)


def add_recipe():
    
    # Generate a random GID
    gid = generate_gid()

    # Initiate the list of ingredients for this specific recipe
    ingredients = []
    
    # Ask for the name of the recipe
    name = click.prompt(click.style("Name?", fg="yellow", bold=True))

    # Ask for the number of guest for the coming recipe
    while True:
        action = click.prompt(click.style("How many people?",
                                           fg="yellow", bold=True))
        if action.isdigit():
            count = int(action)
            break
        else:
            click.secho("Please enter a digit", fg="red", bold=True)

    # Ask for the reference of the recipe
    while True:
        action = click.prompt(click.style("Reference?",
                                           fg="yellow", bold=True))
        reference = str(action)
        break

    # Build the ingredient list
    while True:
        action = click.prompt(click.style("Press 'a' to add an ingredient and 'q' to finish the recipe",
                                           fg="yellow", bold=True))
        if action == "a":
            add_ingredient(ingredients)
        elif action == "q":
            break
        else:
            click.secho("Invalid choice", fg="red", bold=True)

    # Create new recipe
    recipe = Recipe(gid, name, count, reference, ingredients)

    # Add the recipe to the list
    recipes.append(recipe)

    # List updated recipe list
    list_recipes()

    # Record the change to the JSON file
    record_recipes()


def get_recipe_input_key():
    info = ""
    info += "'l' => list the current recipes\n"
    info += "'a' => add new recipe\n"
    info += "'q' => record and quit\n"
    click.secho(info, fg="yellow", bold=True)
    while True:
        action = click.prompt(click.style("Press 'l' to list the recipes, 'a' to add a new one, 'q' to quit",
                                           fg="yellow", bold=True))
        if action == "l":
            list_recipes()
        elif action == "a":
            add_recipe()
        elif action == "q":
            print("Ciao!!")
            exit(0)
        else:
            click.secho("Invalid choice", fg="red", bold=True)
    return confkey


if __name__ == "__main__":
    import sys

# Initialize the list of recipes from the JSON file
data_path = sys.argv[1] + "recipes.json"
db = JManager(data_path)
recipes = db.read_list(Recipe.from_json)
ingredient_path_data = sys.argv[1] + "ingredients.json"
db_ingredients = JManager(ingredient_path_data)
all_ingredients = db_ingredients.read_list(Ingredient.from_json)
units_path_data = sys.argv[1] + "units.json"
db_units = JManager(units_path_data)
all_units = db_units.read_list(Unit.from_json)

# Prompt input from user
get_recipe_input_key()