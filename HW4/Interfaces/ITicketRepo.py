from abc import ABC, abstractmethod
from HW4.Models.Ticket import Ticket


class ITicketRepo(ABC):
    @abstractmethod
    def create(self, ticket: Ticket) -> bool:
        ...

    @abstractmethod
    def read_all(self, route_number) -> list[Ticket]:
        ...

    @abstractmethod
    def update(self, ticket: Ticket) -> bool:
        ...

    @abstractmethod
    def delete(self, ticket: Ticket) -> Ticket:
        ...
