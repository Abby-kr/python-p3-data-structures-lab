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
    food_names = [food.get("name", None) for food in spicy_foods]
    return food_names

def get_spiciest_foods(spicy_foods):
    heat_levels = [food for food in spicy_foods if food.get("heat_level", None) > 5]
    return heat_levels

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food.get("name", None)
        cuisine = food.get("cuisine", None)
        heat_level = food.get("heat_level", None) * "\U0001F336"
        spicy_food = "{} ({}) | Heat Level: {}"
        print(spicy_food.format(name, cuisine, heat_level))

def get_spicy_food_by_cuisine(spicy_foods, cuisine):   
    for food in range(len(spicy_foods)):
    	if spicy_foods[food].get("cuisine",None) == cuisine:
            return spicy_foods[food]

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food.get("heat_level", None) > 5:
            name = food.get("name", None)
            cuisine = food.get("cuisine", None)
            heat_level = food.get("heat_level", None) * "\U0001F336"
            spicy_food = "{} ({}) | Heat Level: {}"
            print(spicy_food.format(name, cuisine, heat_level))

def get_average_heat_level(spicy_foods):
    heat_levels = []
    for food in spicy_foods:
        heat_levels.append(food.get("heat_level", None))
    return sum(heat_levels) / len(heat_levels)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
