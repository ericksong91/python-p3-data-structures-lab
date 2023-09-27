import pdb
from statistics import fmean
spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]


def get_names(spicy_foods):
    new_list = [n["name"] for n in spicy_foods]
    return new_list


def get_spiciest_foods(spicy_foods):
    new_list = [n for n in spicy_foods if n["heat_level"] > 5]
    return new_list


def print_spicy_foods(spicy_foods):
    print_list = [
        print(f'{e["name"]} ({e["cuisine"]}) | Heat Level: ' + ("🌶" * e["heat_level"]))
        for e in spicy_foods
    ]
    return


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    cuisine_food = None
    for foods in spicy_foods:
        if foods["cuisine"] == cuisine:
            cuisine_food = foods
    return cuisine_food


def print_spiciest_foods(spicy_foods):
    for foods in spicy_foods:
        if foods["heat_level"] > 5:
            print(f'{foods["name"]} ({foods["cuisine"]}) | Heat Level: ' + ("🌶" * foods["heat_level"]))
    
    return


def get_average_heat_level(spicy_foods):
    get_spice = [e["heat_level"] for e in spicy_foods]
    return fmean(get_spice)


def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
