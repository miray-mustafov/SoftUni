from project.vehicle import Vehicle
from project.family_car import FamilyCar
from project.car import Car
from project.sport_car import SportCar
from project.race_motorcycle import RaceMotorcycle
from project.motorcycle import Motorcycle
from project.cross_motorcycle import CrossMotorcycle

m = Motorcycle(50, 150)
print(Motorcycle.DEFAULT_FUEL_CONSUMPTION)
print(Motorcycle.DEFAULT_FUEL_CONSUMPTION)
print(m.fuel)
print(m.horse_power)
print(m.fuel_consumption)
m.drive(100)
# print(m.fuel)
# family_car = FamilyCar(150, 150)
# family_car.drive(50)
# print(family_car.fuel)
# family_car.drive(50)
# print(family_car.fuel)
# print(family_car.__class__.__bases__[0].__name__)
