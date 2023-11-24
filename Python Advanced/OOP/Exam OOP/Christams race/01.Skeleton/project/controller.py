from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    CAR_TYPES = {'MuscleCar': MuscleCar,
                  'SportsCar': SportsCar,}
    def __init__(self):
        self.cars=[]
        self.drivers=[]
        self.races=[]

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type not in Controller.CAR_TYPES:
            return

        for car_i in range(len(self.cars)):
            if self.cars[car_i].model  == model:
                raise Exception(f"Car {model} is already created!")


        self.cars.append(Controller.CAR_TYPES[car_type](model, speed_limit))
        return f"{car_type} {model} is created."


    def create_driver(self, driver_name):
        for driver_i in range(len(self.drivers)):
            if self.drivers[driver_i].name == driver_name:
                raise Exception(f"Driver {driver_name} is already created!")

        self.drivers.append(Driver(driver_name))
        return f"Driver {driver_name} is created."


    def create_race(self, race_name):
        for race_i in range(len(self.races)):
            if self.races[race_i].name  == race_name:
                raise Exception(f"Race {race_name} is already created!")

        self.races.append(Race(race_name))


    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver_exists = False
        for dr_i in range(len(self.drivers)):
            if self.drivers[dr_i].name == driver_name:
                driver_exists=True
        if not driver_exists:
            raise Exception(f"Driver {driver_name} could not be found!")

        car_available = None
        for car_i in range(len(self.cars)):
            if self.cars[car_i].__class__.__name__ == car_type and not self.cars[car_i].is_taken:
                car_available = self.cars[car_i]
                break

        if not car_available:
            raise Exception(f"Car {car_type} could not be found!")


        if self.drivers[dr_i].car != None:
            old_model = self.drivers[dr_i].car.model
            new_model = car_available.model
            self.drivers[dr_i].car = car_available
            return f"Driver {driver_name} changed his car from {old_model} to {new_model}."

        self.drivers[dr_i].car = car_available
        return f"Driver {driver_name} chose the car {car_available.model}."

    def add_driver_to_race(self,race_name: str, driver_name: str):
        r_i = Controller.take_idx_or_exception(race_name,self.races)

        d_i = Controller.take_idx_or_exception(driver_name,self.drivers)

        if not self.drivers[d_i].car:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if self.drivers[d_i] in self.races[r_i].drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        self.races[r_i].drivers.append(self.drivers[d_i])
        return f"Driver {driver_name} added in {race_name} race."

    @staticmethod
    def take_idx_or_exception(element,listt):
        listt_names=[el.name for el in listt]
        try:
            idx = listt_names.index(element)
        except(ValueError()):
            raise Exception(f"{listt[0].__class__.__name__} {element} could not be found")

        return idx



    def start_race(self, race_name: str):
        r_i = Controller.take_idx_or_exception(race_name,self.races)
        the_race = self.races[r_i]

        if len(the_race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        # Race started !!!
        # Checking first 3 top speeds

        quee_drivr_SpeedWins = list()
        for drivr in the_race.drivers:
            quee_drivr_SpeedWins.append([drivr.name, drivr.car.speed_limit , drivr.number_of_wins])

        sorted_quee_drivr_SpeedWins = sorted(quee_drivr_SpeedWins, key=lambda x: x[1])

        result = ""
        for dr_i in range(len(sorted_quee_drivr_SpeedWins)-1,-1,-1):
            curr_drivr = sorted_quee_drivr_SpeedWins[dr_i]
            fastest_driver_name = curr_drivr[0]
            speed_limit = curr_drivr[1]

            result += f"Driver {fastest_driver_name} wins the {race_name} race with a speed of {speed_limit}.\n"

        return result



