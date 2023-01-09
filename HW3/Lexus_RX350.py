from car import Car
from refueling import Refueling
from wipe import Wipe


class LexusRX350(Car, Refueling, Wipe):

    def __init__(self, vin_num: str, is_fuel_gasoline: bool, is_gear_box: bool, color: tuple):
        super(LexusRX350, self).__init__()
        self.VIN = vin_num
        self.car_type = self.type_car_dict[3]
        self.fuel_car = self.type_fuel_car[int(is_fuel_gasoline)]
        self.gear_box = self.type_gear_box[int(is_gear_box)]
        self.color = color
        self.model = 'Lexus'
        self.make = 'RX350'
        self.engine_volume = 3.5
        self.engine_volume = 4
        self.capacity = 5  # people

    def fuel(self, fuel_volume: int):  # DI principe не поддерживается
        match self.fuel_car:
            case 'Gasoline':
                ...
            case 'Diesel':
                ...
            case 'Electricity':
                ...

    def move(self, positions: str):
        pass

    def maintenance(self):
        pass

    def switch_gear(self, delta: int):
        pass

    def headlights_on(self):
        pass

    def wipers_on(self):
        pass

    def headlights_off(self):
        pass

    def wipers_off(self):
        pass

    def wip_windshield(self):
        pass

    def wip_headlights(self):
        pass

    def wip_mirrors(self):
        pass

    def climate_control_on(self) -> None:
        pass

    def climate_control_off(self) -> None:
        pass

    def auto_on(self) -> None:
        pass

    def auto_off(self) -> None:
        pass

    def set_volume(self) -> None:
        pass


lexus = LexusRX350('1B3ES66S13D202162', True, True, (255, 0, 0))
# SR principe не нарушается
