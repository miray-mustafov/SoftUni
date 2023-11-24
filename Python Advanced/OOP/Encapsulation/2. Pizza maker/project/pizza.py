from project.dough import Dough
from project.topping import Topping

class Pizza:
    def __init__(self, name: str, dough: Dough, toppings_capacity: int):
        self.name=name
        self.dough=dough
        self.toppings_capacity=toppings_capacity
        self.toppings={}
        self.counter_tops=0

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("The name cannot be an empty string")
        self.__name=value


    @property
    def dough(self):
        return self.__dough
    @dough.setter
    def dough(self, value):
        if not value:
            raise ValueError("You should add dough to the pizza")
        self.__dough=value


    @property
    def toppings_capacity(self):
        return self.__toppings_capacity
    @toppings_capacity.setter
    def toppings_capacity(self, value):
        if value<=0:
            raise ValueError("The topping's capacity cannot be less or equal to zero")
        self.__toppings_capacity=value

    def add_topping(self, topping: Topping):
        self.counter_tops+=1
        if self.counter_tops > self.toppings_capacity:
            raise ValueError("Not enough space for another topping")

        top_name = topping.topping_type
        if top_name not in self.toppings:
            self.toppings[top_name]=topping.weight
        else:
            self.toppings[top_name]+=topping.weight

    def calculate_total_weight(self):
        total_w=self.dough.weight
        total_w+=sum([w for w in self.toppings.values()])
        return total_w