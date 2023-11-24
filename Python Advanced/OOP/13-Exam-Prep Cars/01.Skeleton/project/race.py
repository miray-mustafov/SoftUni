from project.core.validator import Validator


class Race:
    def __init__(self, name):
        self.name = name
        self.drivers = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_if_len_is_less_than(
            value,
            1,
            "Name cannot be an empty string!"
        )
        self.__name = value