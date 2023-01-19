class Carrier:
    def __init__(self, id_: int, card_number: int):
        self.__id_ = id_
        self.__card_number = card_number
        self.__zones = []

    def get_id(self):
        return self.__id_

    def get_card_number(self):
        return self.__card_number
