from ItemGenerator import ItemGenerator
from lumberReward import LumberReward


class LumberGenerator(ItemGenerator):

    def create_item(self, l_border, r_border):
        return LumberReward(l_border, r_border)
