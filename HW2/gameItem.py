from abc import ABC, abstractmethod


# interface class
class GameItem(ABC):

    def __init__(self, l_border, r_border):
        self.l_border = l_border
        self.r_border = r_border

    @abstractmethod
    def open_item(self):
        pass
