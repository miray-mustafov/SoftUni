from project.food.main_dish import MainDish


class Salmon(MainDish):

    GRAMS = 22  #Applied to all salmons attribute grams musn't be mutable

    def __init__(self, name, price):
        super().__init__(name, price, Salmon.GRAMS)