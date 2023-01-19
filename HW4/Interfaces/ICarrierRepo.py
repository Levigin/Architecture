from abc import ABC, abstractmethod
from HW4.Models.Carrier import Carrier


class ICarrierRepo(ABC):

    @abstractmethod
    def read(self, id_) -> Carrier:
        ...
