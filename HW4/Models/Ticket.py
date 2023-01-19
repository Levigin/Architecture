from datetime import datetime


class Ticket:

    def __init__(self, route_number: int, place: int, price: int, date: datetime, is_valid: bool):
        self.__route_number = route_number
        self.__place = place
        self.__price = price
        self.__date = date
        self.__is_valid = is_valid
        self.__zone_start = None
        self.__zone_stop = None

    def __str__(self):
        return f"Ticket: \nroute_number: {self.__route_number} \nplace: {self.__place} \nprice: {self.__price} " \
               f"\ndate: {self.__date} \n{('Free' if self.__is_valid else 'Busy')}"

    def __hash__(self):
        return hash(self.__date) ^ (self.__route_number + self.__price + self.__place)

    def __eq__(self, other):
        if other is None or type(other) != type(self):
            return False
        else:
            return self.__route_number == other.__route_number and self.__place == other.__place and\
                   self.__price == other.__price and self.__date == other.__date and hash(self) == hash(other)

    def get_route_number(self):
        return self.__route_number

    def get_place(self):
        return self.__place

    def get_price(self):
        return self.__price

    def get_date(self):
        return self.__date

    def get_is_valid(self):
        return self.__is_valid

    def set_valid(self, flag: bool):
        self.__is_valid = flag

    def set_zone_start(self, zone_start):
        self.__zone_start = zone_start

    def set_zone_stop(self, stop):
        self.__zone_stop = stop
