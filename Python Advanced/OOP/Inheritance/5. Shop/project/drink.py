from project.product import Product


class Drink(Product):
    def __init__(self, name, quantity):
        super().__init__(name, 15)
        