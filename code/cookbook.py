from typing import List
import json


class Ingredient:

    def __init__(self, gid: object):
        self.gid = gid

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
