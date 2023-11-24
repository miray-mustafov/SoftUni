from Bakery.project.baked_food.bread import Bread
from Bakery.project.baked_food.cake import Cake


class Bakery:
    def __init__(self, name):
        self.name = name

        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0


    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Name cannot be empty string or white space!")
        self.__name=value

    def add_food(self, food_type: str, name: str, price: float):
        if any(f.name == name for f in self.food_menu):
            raise Exception(f"{food_type} {name} is already in the menu!")

        baked_foods = {"Bread" : Bread, "Cake": Cake}

        food_to_add = baked_foods[food_type](name, price)
        self.food_menu.append(food_to_add)
        return f"Added {name} ({food_type}) to the food menu"

