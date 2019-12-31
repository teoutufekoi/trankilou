import json
from collections import namedtuple


class Ingredient:

    def __init__(self, jdata: object, gid: object):
        if jdata is not None:
            self.__dict__ = json.loads(jdata)
        else:
            self.gid = gid
            self.domain = "no domain"
            self.unit = "no unit"
            self.season = "no season"
            self.language = "french"


def write_json(data, fn):
    with open(fn, 'w') as f:
        json.dump(data, f)


def read_json(fn):
    with open(fn) as json_file:
        data = json.load(json_file)
        return data


recipes = []
rec1 = {'name': 'Tarte au fromage'}
rec2 = {'name': 'Tarte au chèvre'}
recipes.append(rec1)
recipes.append(rec2)

json_string = json.dumps(recipes)

filename = "data.json"

write_json(json_string, filename)

recipes2 = read_json(filename)

# print(recipes2)

if __name__ == "__main__":
    import sys

    print(sys.argv)

name = input("Please enter the new recipe name : ")

butter = Ingredient(None, 1)
butter.domain = "fresh goods"

print(butter)
print(butter.domain)

json_string = json.dumps(butter.__dict__)

filename2 = "class_dump"

write_json(json_string, filename2)

json_data = read_json(filename2)

butter2 = Ingredient(json_data, None)

print(butter2)
print(butter2.domain)