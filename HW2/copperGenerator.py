from ItemGenerator import ItemGenerator
from copperReward import CopperReward


class CopperGenerator(ItemGenerator):

    def create_item(self, l_border, r_border):
        return CopperReward(l_border, r_border)
