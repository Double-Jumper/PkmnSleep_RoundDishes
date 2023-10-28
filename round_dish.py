from dish_data import ingredients, all_dishes
from math import floor
import itertools
import time

class CookingStats:
    levels = None
    dishes = None
    area_bonus = None
    pot_size = None

    def __init__(self, dish_type: str, pot_size: int, area_bonus=0):
        self.load_levels()
        self.dishes = all_dishes[dish_type]
        self.pot_size = pot_size
        self.area_bonus = area_bonus

    def load_levels(self, file="dish_levels.txt"):
        with open(file, 'r') as f:
            lines = f.readlines()
            self.levels = {
                dish:int(level) for (dish,level) in 
                [line.split(':') for line in lines]
            }

    #Not implemented: mixed dishes, counting crits
    def get_dish_str(self, name: str, extra_ings: dict):
        selected_ings = dict(extra_ings)
        dish = self.dishes[name]
        if dish["amount"] > self.pot_size:
            return None
        level = self.levels[name]
        base_recipe_strength = dish["power"][level-1]
        extra_ing_power = sum(
            ingredients[ing]*amount for (ing,amount) in selected_ings.items()
        )
        strength = floor(
            round(base_recipe_strength + extra_ing_power)*(1+(area_bonus/100))
        )
        return strength
    
    def brute_force_round_dishes(self, bag: dict, minimum_size: int):
        bag = {ing:amount for (ing,amount) in bag.items() if amount > 0}
        results = []
        for dish, info in self.dishes.items():
            current_bag = dict(bag)
            req_ings = info["ingredients"]
            #Discard dishes that can't be made
            if not all(ing in current_bag and 
                current_bag[ing]>=amount for (ing,amount) in req_ings.items()
            ):
                continue
            #Remove ings from base recipe
            for (ing, amount) in req_ings.items():
                current_bag[ing] -= amount
                if current_bag[ing] == 0:
                    current_bag.pop(ing)
            available_slots = self.pot_size - info["amount"]
            if available_slots < 0:
                continue
            #Thanks to SciresM for this lambda, generates ways that up to
            # X things can be divided into N columns
            # In this case, X = available slots, N = types of ingredients
            F = lambda X, Y, N: itertools.filterfalse(
                lambda t: sum(t) > X or sum(t) < Y, itertools.product(range(X+1), repeat=N)
            )
            minimum_extras = minimum_size-info["amount"]
            for t in F(available_slots, minimum_extras, len(current_bag)):
                if not all(
                    list(current_bag.values())[i] >= amount for (i,amount) in enumerate(t)
                ):
                    continue
                attempt_items = {ing:t[i] for i,ing in enumerate(current_bag)}
                strength = self.get_dish_str(dish, attempt_items)
                if strength % 1000 == 0:
                    results.append([dish, strength, attempt_items])
        return results



# dish_type = "curries"
# dish_type = "salads"
dish_type = "desserts"
pot_size = 39
minimum_size = 35
area_bonus = 25 #0-100 number
stats = CookingStats(dish_type, pot_size, area_bonus)
bag = {
    "Leek": 0,
    "Mushroom": 0,
    "Egg": 0,
    "Potato": 8,
    "Apple": 0,
    "Herb": 0,
    "Sausage": 9,
    "Milk": 15,
    "Honey": 0,
    "Oil": 5,
    "Ginger": 15,
    "Tomato": 15,
    "Cacao": 0,
    "Tail": 0,
    "Soybeans": 0
}
start = time.time()
results = stats.brute_force_round_dishes(bag, minimum_size)
max_dish = max(results, key=lambda x: x[1])
max_dishes = [r for r in results if r[1]==max_dish[1]]
print(max_dishes)
elapsed = time.time()-start
print(elapsed)
