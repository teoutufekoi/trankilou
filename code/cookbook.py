from typing import List
import json


class Label:

    def __init__(self, gid: object, name: object):
        self.gid = gid
        self.name = name

    @classmethod
    def from_json(cls, data):
        return cls(**data)


class Domain:

    def __init__(self, gid: object, name: object):
        self.gid = gid
        self.name = name

    @classmethod
    def from_json(cls, data):
        return cls(**data)


class Unit:

    def __init__(self, gid: object, name: object, short: object):
        self.gid = gid
        self.name = name
        self.short = short

    @classmethod
    def from_json(cls, data):
        return cls(**data)


class Ingredient:

    def __init__(self, gid: object, name: object, domain: object, unit: object):
        self.gid = gid
        self.name = name
        self.domain = domain
        self.unit = unit

    @classmethod
    def from_json(cls, data):
        return cls(**data)


class Recipe:

    def __init__(self, gid: int, name: str, count: int, reference: int, ingredients: List[int],
                 labels: List[str], date: str, author: str):
        self.gid = gid
        self.name = name
        self.count = count
        self.reference = reference
        self.ingredients = ingredients
        self.labels = labels
        self.date = date
        self.author = author

    def add_ingredient(self, ingredient):
        # TODO merge ingredients if the ingredient is alreday part of the list
        self.ingredients.append(ingredient)

    def add_label(self, label):
        if label not in self.labels:
            self.labels.append(label)

    @classmethod
    def from_json(cls, data):
        return cls(**data)


class SelectedRecipe:

    def __init__(self, gid: int, count: int):
        self.gid = gid
        self.count = count

    @classmethod
    def from_json(cls, data):
        return cls(**data)


class ShoppingList:

    def __init__(self, gid: int, name: str, recipes: List[SelectedRecipe]):
        self.gid = gid
        self.name = name
        self.recipes = recipes

    @classmethod
    def from_json(cls, data):
        gid = data["gid"]
        name = data["name"]
        recipes = list(map(SelectedRecipe.from_json, data["recipes"]))
        return cls(gid, name, recipes)


class CookBook:

    def __init__(self, recipes: List[Recipe], ingredients: List[Ingredient]):
        self.recipes = recipes
        self.ingredients = ingredients

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    @classmethod
    def from_json(cls, data):
        recipes = list(map(Recipe.from_json, data["recipes"]))
        ingredients = list(map(Ingredient.from_json, data["ingredients"]))
        return cls(recipes, ingredients)
