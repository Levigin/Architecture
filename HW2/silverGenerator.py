from ItemGenerator import ItemGenerator
from silverReward import SilverReward


class SilverGenerator(ItemGenerator):

    def create_item(self, l_border, r_border):
        return SilverReward(l_border, r_border)
