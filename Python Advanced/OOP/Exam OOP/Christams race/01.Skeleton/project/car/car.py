from abc import ABC, abstractmethod


class Car:
    @abstractmethod
    def __init__(self, model, speed_limit: int, min_sp_lim=None, max_sp_lim=None):
        self.model = model
        self.min_sp_lim = min_sp_lim # w8ts params from daughter classes
        self.max_sp_lim = max_sp_lim
        self.speed_limit = speed_limit

        self.is_taken = False  #ONLY one driver per car

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if len(value) < 4:
            raise ValueError(f"Model {value} is less than 4 symbols!")
        self.__model = value

    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, value):
        if value not in range(self.min_sp_lim, self.max_sp_lim):
            raise ValueError(f"Invalid speed limit! Must be between {self.min_sp_lim} and {self.max_sp_lim}!")
        self.__speed_limit = value