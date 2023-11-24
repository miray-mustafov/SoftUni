from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    car_types = {
        "MuscleCar": MuscleCar,
        "SportsCar": SportsCar
    }

    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type not in Controller.car_types:
            return  # ignore command

        search = [car.model == model for car in self.cars]
        if any(search):
            raise Exception(f"Car {model} is already created!")

        new_car = Controller.car_types[car_type](model, speed_limit)
        self.cars.append(new_car)

        return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        search = [driver.name == driver_name for driver in self.drivers]
        if any(search):
            raise Exception(f"Driver {driver_name} is already created!")

        new_driver = Driver(driver_name)
        self.drivers.append(new_driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        search = [race.name == race_name for race in self.races]
        if any(search):
            raise Exception(f"Driver {race_name} is already created!")

        new_race = Race(race_name)
        self.races.append(new_race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        curr_driver = [driver for driver in self.drivers if driver.name == driver_name]
        if not curr_driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        curr_driver = curr_driver[0]
        curr_driver_current_car = curr_driver.car
        # search_car = [car.__class__.__name__ == car_type for car in self.cars]
        # search_car_istaken = [car.is_taken for car in self.cars if car.__class__.__name__ == car_type]
        # if not all(search_car) or all(search_car_istaken):
        #     raise f"Car {car_type} could not be found!"

        for i in range(len(self.cars) - 1, -1, -1):
            curr_car = self.cars[i]
            if curr_car.__class__.__name__ == car_type and curr_car.is_taken is False:
                if curr_driver.car is not None:
                    message = f"Driver {driver_name} changed his car from {curr_driver.car.model} to {curr_car.model}."
                    curr_driver.car = curr_car
                else:  # demek drivera nqma kola
                    curr_driver.car = curr_car
                    message = f"Driver {driver_name} chose the car {curr_car.model}."

                curr_car.is_taken = True  # !!!
                return message

        #  ako drivera nishto ne mu se e promenilo => ne e nameril kola
        if curr_driver.car == curr_driver_current_car:
            raise Exception(f"Car {car_type} could not be found!")

    # def add_driver_to_race(self, race_name: str, driver_name: str):


controller = Controller()
print(controller.create_driver("Peter"))
print(controller.create_car("SportsCar", "Porsche 718 Boxster", 470))
print(controller.add_car_to_driver("Peter", "SportsCar"))
print(controller.create_car("SportsCar", "Porsche 911", 580))
print(controller.add_car_to_driver("Peter", "SportsCar"))
