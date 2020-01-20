import click
import binascii
import os
from cookbook import *
from database import *
from helpers import *


def list_shopping_lists():
    for i in range(len(shopping_lists)):
        print("- " + str(i) + " - " + str(shopping_lists[i].name))


def add_ingredient(key, ingredients):
    print("Adding the ingredient XXX")


def get_ingredients_from_recipe(original_recipe, actual_count):

    # Init the dict of ingredients
    ingredients = {}

    # Fill the dict of ingredients
    print("Ingredients in the recipe " + original_recipe.name + ":")
    for ingredient in original_recipe.ingredients:
        gid = ingredient["gid"]
        quantity = ingredient["quantity"]
        ingredients[gid] = {}
        ingredients[gid]["quantity"] = quantity
        print(str(ingredients[gid]))

    return ingredients


def get_ingredients_from_recipes(recipes):

    # Init the dict of ingredients
    ingredients = {}

    for recipe in recipes:
        original_recipe = get_recipe(recipe.gid, all_recipes)
        new_ingredients = get_ingredients_from_recipe(original_recipe, recipe.count)
        ingredients.update(new_ingredients)
    return ingredients


def print_shopping_list(shopping_list):
    # Get the list of ingredients
    ingredients = get_ingredients_from_recipes(shopping_list.recipes)

    # Print the ingredients
    print("List of ingredients the selected shopping list:")
    for ingredient in ingredients:
        print(ingredient)


def get_shopping_list_input_key():
    info = "Select the shopping list you want to print\n"
    info += "'q' => quit\n"
    click.secho(info, fg="yellow", bold=True)
    list_shopping_lists()
    while True:
        user_input = click.prompt(click.style("Select the number of the list to print, 'q' to quit",
                                           fg="yellow", bold=True))
        if user_input.isdigit() and int(user_input) < len(shopping_lists):
            print_shopping_list(shopping_lists[int(user_input)])
        elif user_input == "q":
            print("Ciao!!")
            exit(0)
        else:
            click.secho("Invalid choice", fg="red", bold=True)
    return confkey


if __name__ == "__main__":
    import sys

# Initialize the list of recipes from the JSON file
data_path = sys.argv[1] + "shopping_lists.json"
db = JManager(data_path)
shopping_lists = db.read_list(ShoppingList.from_json)
recipe_path_data = sys.argv[1] + "recipes.json"
db_recipes = JManager(recipe_path_data)
all_recipes = db_recipes.read_list(Recipe.from_json)
ingredient_path_data = sys.argv[1] + "ingredients.json"
db_ingredients = JManager(ingredient_path_data)
all_ingredients = db_ingredients.read_list(Ingredient.from_json)
units_path_data = sys.argv[1] + "units.json"
db_units = JManager(units_path_data)
all_units = db_units.read_list(Unit.from_json)
domains_path_data = sys.argv[1] + "domains.json"
db_domains = JManager(domains_path_data)
all_domains = db_domains.read_list(Domain.from_json)

# Prompt input from user
get_shopping_list_input_key()