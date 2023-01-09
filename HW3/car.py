from abc import ABC, abstractmethod


class Car(ABC):

    type_car_dict = {0: 'Sedan', 1: 'Pickup', 2: 'Hatchback', 3: 'Crossover'}
    type_fuel_car = {0: 'Gasoline', 1: 'Diesel', 2: 'Electricity'}
    type_gear_box = {0: 'MT', 1: 'AT'}

    def __init__(self):
        self.make = None
        self.model = None
        self.color = None
        self.car_type = None
        self.fuel_car = None
        self.gear_box = None
        self.wheels_quantity = None
        self.engine_volume = None
        self.VIN = None

    @abstractmethod
    def move(self, position: str) -> bool:  # moves the car to the position chosen
        ...

    @abstractmethod
    def maintenance(self) -> int:  # hours of maintenance
        ...

    @abstractmethod
    def switch_gear(self, delta: int) -> bool:
        # returns True  if gear has been switched successfully and False otherwise
        ...

    @abstractmethod
    def headlights_on(self) -> None:
        ...

    @abstractmethod
    def wipers_on(self) -> None:
        ...

    @abstractmethod
    def headlights_off(self) -> None:
        ...

    @abstractmethod
    def wipers_off(self) -> None:
        ...
