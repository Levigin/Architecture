class BankAccount:

    def __init__(self, card_number: int):
        self.__card = card_number
        self.__balance = 1000  # $

    def __str__(self):
        return f'BankAccount {self.__card}, balance: {self.__balance}'

    def __repr__(self):
        return str(self)

    def set_balance(self, new_balance: int):
        self.__balance = new_balance

    def get_card(self):
        return self.__card

    def get_balance(self):
        return self.__balance

