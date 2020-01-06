from typing import List
import json

class Doamin:

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

    def __init__(self, gid: int, name: str, ingredients: List[int]):
        self.gid = gid
        self.name = name
        self.ingredients = ingredients

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    @classmethod
    def from_json(cls, data):
        return cls(**data)


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
