from ItemGenerator import ItemGenerator
from platinumReward import PlatinumReward


class PlatinumGenerator(ItemGenerator):

    def create_item(self, l_border, r_border):
        return PlatinumReward(l_border, r_border)
