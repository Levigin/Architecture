import gameItem
from abc import ABC, abstractmethod


# abstract class
class ItemGenerator(ABC):

    def __init__(self, l_border, r_border):
        self.l_border = l_border
        self.r_border = r_border

    @abstractmethod
    def create_item(self, l_border, r_border) -> gameItem.GameItem:
        pass

    def open_reward(self):
        game_item = self.create_item(self.l_border, self.r_border)
        game_item.open_item()
