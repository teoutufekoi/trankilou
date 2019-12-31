from cookbook import *
from database import *

if __name__ == "__main__":
    import sys

    print(sys.argv)

db = JManager(sys.argv[1])
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
print(data)
db.record(data)

# Deserializing

decoded_cookbook = CookBook.from_json(json.loads(data))
print(decoded_cookbook)
print(decoded_cookbook.recipes)



