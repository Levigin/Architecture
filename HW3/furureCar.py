from car import Car


class FutureCar(Car):

    def __init__(self):
        super(FutureCar, self).__init__()
        # self.wheels_quantity = 3  --> LS principe нарушается

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

    def fly(self, positions: str) -> None:
        # LS principe не нарушается
        pass
