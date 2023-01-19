from HW4.Services.CarrierRepository import CarrierRepository
from HW4.Services.CashRepository import CashRepository
from HW4.Models.User import User
from HW4.ClientApplication.Authentication import Authentication
from HW4.Core.UserProvider import UserRepository


class CashProvider:

    def __init__(self, card_number):
        self.carrier_repository = CarrierRepository.get_carrier_repository()
        self.cash_repository = CashRepository.get_cash_repository()
        self.card_number = card_number
        self.is_authorized = False

    def buy(self, ticket):
        carrier = self.carrier_repository.read(1)
        return self.cash_repository.transaction(ticket.get_price(), self.card_number, carrier.get_card_number())

    def authorization(self, client: User):
        self.is_authorized = Authentication.authentication(UserRepository(), client.get_user_name(),
                                                           client.get_hash_password())

