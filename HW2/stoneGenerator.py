from ItemGenerator import ItemGenerator
from stoneReward import StoneReward


class StoneGenerator(ItemGenerator):

    def create_item(self, l_border, r_border):
        return StoneReward(l_border, r_border)
