import click
import binascii
import os
from datetime import datetime
from cookbook import *
from database import *
from helpers import *



def list_shopping_lists():
    for i in range(len(shopping_lists)):
        print("- " + str(i) + " - " + str(shopping_lists[i].name))


def get_ingredients_from_recipe(original_recipe, ratio):

    # Init the dict of ingredients
    ingredients = {}

    # Fill the dict of ingredients
    print("Adding ingredients from recipe '" + original_recipe.name + "' (ratio " + str(ratio) + ")")
    for ingredient in original_recipe.ingredients:
        gid = ingredient["gid"]
        quantity = ingredient["quantity"] * ratio
        ingredient = get_ingredient(gid, all_ingredients)
        unit = get_unit(ingredient.unit, all_units)
        domain = get_domain(ingredient.domain, all_domains)
        ingredients[gid] = {}
        ingredients[gid]["quantity"] = quantity
        ingredients[gid]["name"] = ingredient.name
        ingredients[gid]["unit"] = unit
        ingredients[gid]["domain"] = domain.name
        ingredients[gid]["recipes"] = [original_recipe.name]

    return ingredients


def add_new_ingredients(new_ingredients, ingredients):
    # Add new ingredients one after each other
    for new_ingredient in new_ingredients:
        if new_ingredient in ingredients:
            # Sum the ingredient quantities
            ingredients[new_ingredient]["quantity"] += new_ingredients[new_ingredient]["quantity"]
            # Append the recipe to the recipe list for the current ingredient
            ingredients[new_ingredient]["recipes"].append(new_ingredients[new_ingredient]["recipes"][0])
        else:
            # Add ingredient in the dict of ingredients
            ingredients[new_ingredient] = new_ingredients[new_ingredient]

    return ingredients


def get_ingredients_from_recipes(recipes):

    # Init the dict of ingredients
    ingredients = {}

    for recipe in recipes:
        original_recipe = get_recipe(recipe.gid, all_recipes)
        ratio = recipe.count / original_recipe.count
        new_ingredients = get_ingredients_from_recipe(original_recipe, ratio)
        ingredients = add_new_ingredients(new_ingredients, ingredients)

    return ingredients


def print_shopping_list(shopping_list):
    # Get the list of ingredients
    ingredients = get_ingredients_from_recipes(shopping_list.recipes)

    # Build the string to be printed in the output file
    s = shopping_list.name + "\n"
    s += str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")) + "\n"

    # Update the string with the list of recipes included
    for r in shopping_list.recipes:
        original_recipe = get_recipe(r.gid, all_recipes)
        s += original_recipe.name + " (" + str(int(r.count)) + " pp)" +"\n"

    # Update the string with the ingredients for each domain
    for domain in all_domains:
        sublist = dict(filter(lambda elem: elem[1]["domain"] == domain.name, ingredients.items()))
        s += "\n------ " + domain.name + " ------\n\n"
        for i in sublist:
            ingredient = sublist[i]
            s += ingredient["name"] + " - " + str(round(ingredient["quantity"],1)) + " " + ingredient["unit"] + "\n"

    # Print to output file
    text_file = open("out.txt", "w")
    text_file.write(s)
    text_file.close()


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