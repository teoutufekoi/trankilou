from cookbook import *
from database import *

if __name__ == "__main__":
    import sys

data_path = sys.argv[1]
db = JManager(data_path + "data.json")
json_data = db.read()
cookbook = CookBook.from_json(json.loads(json_data))

print(cookbook)

butter = Ingredient(123)
milk = Ingredient(124)
cheesecake = Recipe(234, "cheesecake", [])
cheesecake.add_ingredient(butter.gid)
cheesecake.add_ingredient(milk.gid)

cookbook = CookBook(recipes=[cheesecake], ingredients=[butter, milk])

# Serializing

data = json.dumps(cookbook, default=lambda o: o.__dict__, sort_keys=True, indent=4)
# print(data)
db.record(data)

# Deserializing

decoded_cookbook = CookBook.from_json(json.loads(data))
# print(decoded_cookbook)
# print(decoded_cookbook.recipes)

# Tests on Ingredient List

ingredients = [butter, milk]
db2 = JManager(data_path + "ingredients.json")
db2.record_list(ingredients)
decoded_ingredients = db2.read_list(Ingredient.from_json)
print(decoded_ingredients[0].gid)
