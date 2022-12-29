from ItemGenerator import ItemGenerator
from goldReward import GoldReward


class GoldGenerator(ItemGenerator):

    def create_item(self, l_border, r_border):
        return GoldReward(l_border, r_border)
