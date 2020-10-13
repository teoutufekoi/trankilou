import click
import binascii
import os
import csv
from cookbook import *
from database import *
from datetime import date

def csvheader():
    header = []
    # Start with recipe main attributes
    header.append('gid')
    header.append('name')
    header.append('author')
    header.append('date')
    # Add labels
    for i in range(len(all_labels)):
        header.append(all_labels[i].name)
    # Add labels
    for i in range(len(all_ingredients)):
        header.append(all_ingredients[i].name)

    return header


def export2csv():

    # Item to export
    items = []

    # header
    header = csvheader()

    # Build the list of recipes
    recipes = []
    for recipe in all_recipes:
        recipe_row = {}
        recipe_row['gid'] = recipe.gid
        recipe_row['name'] = recipe.name
        recipe_row['author'] = recipe.author
        recipe_row['date'] = recipe.date
        recipes.append(recipe_row)

        # Add labels information
        for i in range(len(all_labels)):
            # Get to know if the label is currently associated with the recipe
            recipe_row[all_labels[i].name] = "1" if all_labels[i].gid in recipe.labels else "0"
    
        # Add ingredients information
        for i in range(len(all_ingredients)):
            # Get to know if the label is currently associated with the recipe
            ingredient_gids = [ x['gid'] for x in recipe.ingredients]
            recipe_row[all_ingredients[i].name] = "1" if all_ingredients[i].gid in ingredient_gids else "0"
    # all_ingredients_list = []
    # for i in range(len(all_ingredients)):
    #     s = "- " + str(i) + " - " + str(all_ingredients[i].name) + " (" + get_unit(str(all_ingredients[i].unit)) + ")"
    #     all_ingredients_list.append(s)
    #     print(s)
 
    # Write content to csv file
    with open('out.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter='\t', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        # Export the header
        spamwriter.writerow(header)
        # Export the list
        for recipe in recipes:
            spamwriter.writerow(recipe.values())


def export_recipes():
    
    # Ask for the exportation method
    info = ""
    info += "'csv' => export to csv file\n"
    info += "'google' => update googlesheet\n"
    info += "'q' => record and quit\n"
    click.secho(info, fg="yellow", bold=True)
    while True:
        action = click.prompt(click.style("Press 'csv' to export into csv file and 'google' to export to googlesheet",
                                           fg="yellow", bold=True))
        if action == "csv":
            export2csv()
        elif action == "google":
            break
        elif action == "q":
            print("Ciao!!")
            exit(0)
        else:
            click.secho("Invalid choice", fg="red", bold=True)

    
if __name__ == "__main__":
    import sys

# Initialize the list of recipes from the JSON file
data_path = sys.argv[1] + "recipes.json"
db = JManager(data_path)
all_recipes = db.read_list(Recipe.from_json)
ingredient_path_data = sys.argv[1] + "ingredients.json"
db_ingredients = JManager(ingredient_path_data)
all_ingredients = db_ingredients.read_list(Ingredient.from_json)
units_path_data = sys.argv[1] + "units.json"
db_units = JManager(units_path_data)
all_units = db_units.read_list(Unit.from_json)
labels_path_data = sys.argv[1] + "labels.json"
db_labels = JManager(labels_path_data)
all_labels = db_labels.read_list(Label.from_json)

# Prompt input from user
export_recipes()