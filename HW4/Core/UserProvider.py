from HW4.Interfaces.IUserRepo import IUserRepo
from HW4.Services.UserRepository import UserRepository


class UserProvider:

    def __init__(self):
        self.client_repository = UserRepository.get_client_repository()

    def create_client(self, user_name, password_hash, card_number):
        return self.client_repository.create(user_name, password_hash, card_number)

    def get_all_clients(self):
        return self.client_repository.read_all()
