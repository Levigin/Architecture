import random

from HW4.Interfaces.ICashRepo import ICashRepo
from HW4.Models.BankAccount import BankAccount


class CashRepository:
    __cash_repository = None

    def __init__(self):
        self.__clients = []
        for i in range(1, 6):
            self.__clients.append(BankAccount(random.randrange(10 ** 16, 10 ** 17 - 1)))

    def get_clients(self) -> list[BankAccount]:
        return self.__clients

    @staticmethod
    def get_cash_repository() -> 'CashRepository':
        if CashRepository.__cash_repository is None:
            CashRepository.__cash_repository = CashRepository()
        return CashRepository.__cash_repository

    def transaction(self, payment: int, card_from: int, carrier_card: int):
        from_ = None
        to_ = None
        for client in self.__clients:
            if client.get_card() == card_from:
                from_ = client
            if client.get_card() == carrier_card:
                to_ = client
        if from_ is None:
            raise Exception("No withdrawal account")
        if to_ is None:
            raise Exception("No many account")

        if from_.get_balance() == - payment < 0:
            raise Exception('No many')

        try:
            pass
        finally:
            self.__clients.remove(from_)
            self.__clients.remove(to_)
            from_.set_balance(from_.get_balance() - payment)
            to_.set_balance(to_.get_balance() + payment)
            self.__clients.append(from_)
            self.__clients.append(to_)
