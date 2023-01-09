from abc import ABC, abstractmethod


class Wipe(ABC):

    @abstractmethod
    def wip_windshield(self) -> None:
        ...

    @abstractmethod
    def wip_headlights(self) -> None:
        ...

    @abstractmethod
    def wip_mirrors(self) -> None:
        ...
