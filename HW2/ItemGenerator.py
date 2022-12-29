import gameItem


# abstract class
class ItemGenerator:

    def __init__(self, l_border, r_border):
        self.l_border = l_border
        self.r_border = r_border

    def create_item(self, l_border, r_border) -> gameItem.GameItem:
        pass

    def open_reward(self):
        game_item = self.create_item(self.l_border, self.r_border)
        game_item.open_item()