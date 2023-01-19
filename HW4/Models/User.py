class User:

    def __init__(self, id_: int, user_name: str, hash_password: int, card_number: int):
        self.__id_ = id_
        self.__user_name = user_name
        self.__hash_password = hash_password
        self.__card_number = card_number

    def __str__(self):
        return f"Client id: {self.__id_}, user_name: {self.__user_name}, card_number: {self.__card_number}"

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if other is None or type(other) != type(self):
            return False
        else:
            return self.__id_ == other.__id_ and self.__user_name == other.__user_name and\
                   self.__hash_password == other.__hash_password and self.__card_number == other.__card_number

    def __hash__(self):
        return hash((self.__hash_password,  self.__user_name, self.__id_, self.__card_number))

    def get_id(self):
        return self.__id_

    def get_user_name(self):
        return self.__user_name

    def get_card_number(self):
        return self.__card_number

    def get_hash_password(self):
        return self.__hash_password
