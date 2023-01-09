from ItemGenerator import ItemGenerator
from ironReward import IronReward


class IronGenerator(ItemGenerator):

    def create_item(self, l_border, r_border):
        return IronReward(l_border, r_border)
