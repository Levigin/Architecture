from ItemGenerator import ItemGenerator
from sulfurReward import SulfurReward


class SulfurGenerator(ItemGenerator):

    def create_item(self, l_border, r_border):
        return SulfurReward(l_border, r_border)
