from cookbook import *
from database import *

if __name__ == "__main__":
    import sys

    print(sys.argv)

db = JManager(sys.argv[1])
# json_data = db.read()
butter = Ingredient(None, 121)
milk = Ingredient(None, 123)

ingredients = [butter, milk]

json_string = json.dumps(ingredients, indent=4)
print(json_string)
db.record(json_string)

json_data = db.read()

# ingredients = Ingredient(json_data, None)
ingredients = json.loads(json_data)
