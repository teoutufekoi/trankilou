import click
import binascii
import os
from cookbook import *
from database import *
from helpers import *


def list_shopping_lists():
    for i in range(len(shopping_lists)):
        print(shopping_lists[i].name)


def record_shopping_lists():
    db.record_list(shopping_lists)


def add_ingredient(key, ingredients):
    print("Adding the ingredient XXX")


def get_ingredients_from_recipes(recipes):
    ingredients = []
    return ingredients

def filter_recipes(recipe, str_input):
    if str_input.lower() in recipe.lower():
        return True
    else:
        return False

def add_recipe(recipes):
    # Initiate the recipe structure
    recipe = {}

    # Ask for the recipe using the list of existing recipes
    all_recipes_list = []
    for i in range(len(all_recipes)):
        s = "- " + str(i) + " - " + str(all_recipes[i].name)
        all_recipes_list.append(s)
        print(s)

    # Select the recipe
    while True:
        # Ask for input (select ingredient or filter the list)
        action = click.prompt(click.style("Select a recipe",
                                          fg="yellow", bold=True))
        if action.isdigit() and float(action) < len(all_recipes):
            recipe["gid"] = all_recipes[int(action)].gid
            break
        else:
            filtered_recipes = filter(lambda seq: filter_recipes(seq, action), all_recipes_list)
            for recipe_str in filtered_recipes:
                print(recipe_str)
            #click.secho("Please select a recipe using a proper index.", fg="red", bold=True)

    # Select the quantity
    while True:
        action = click.prompt(click.style("Select the amount of guests",
                                          fg="yellow", bold=True))
        if action.isdigit():
            recipe["count"] = float(action)
            break
        else:
            click.secho("Please enter a number.", fg="red", bold=True)

    # Add the recipe to the list
    recipes.append(recipe)


def add_shopping_list():
    # Generate a random GID
    gid = generate_gid()

    # Initiate the list of recipes for this specific shopping list
    recipes = []

    # Ask for the name of the shopping list
    name = click.prompt(click.style("Name?", fg="yellow", bold=True))

    # Build the recipe list
    while True:
        action = click.prompt(click.style("Press 'a' to add a recipe and 'q' to finish the shopping list",
                                           fg="yellow", bold=True))
        if action == "a":
            add_recipe(recipes)
        elif action == "q":
            break
        else:
            click.secho("Invalid choice", fg="red", bold=True)

    # Create new shopping list
    shopping_list = ShoppingList(gid, name, recipes)

    # Add the recipe to the list
    shopping_lists.append(shopping_list)

    # List updated recipe list
    list_shopping_lists()

    # Record the change to the JSON file
    record_shopping_lists()

def get_shopping_list_input_key():
    info = ""
    info += "'l' => list the current shopping lists\n"
    info += "'a' => add a new shopping list\n"
    info += "'q' => quit\n"
    click.secho(info, fg="yellow", bold=True)
    while True:
        action = click.prompt(click.style("Press 'l' to list the shopping lists, 'a' to add a new one, 'q' to quit",
                                           fg="yellow", bold=True))
        if action == "l":
            list_shopping_lists()
        elif action == "a":
            add_shopping_list()
        elif action == "q":
            print("Ciao!!")
            exit(0)
        else:
            click.secho("Invalid choice", fg="red", bold=True)
    return confkey


if __name__ == "__main__":
    import sys

# Initialize the list of recipes from the JSON file
data_path = "src/data/shopping_lists.json"
db = JManager(data_path)
shopping_lists = db.read_list(ShoppingList.from_json)
recipe_path_data = "src/data/recipes.json"
db_recipes = JManager(recipe_path_data)
all_recipes = db_recipes.read_list(Recipe.from_json)
# ingredient_path_data = sys.argv[1] + "ingredients.json"
# db_ingredients = JManager(ingredient_path_data)
# all_ingredients = db_ingredients.read_list(Ingredient.from_json)
# units_path_data = sys.argv[1] + "units.json"
# db_units = JManager(units_path_data)
# all_units = db_units.read_list(Unit.from_json)

# Prompt input from user
get_shopping_list_input_key()