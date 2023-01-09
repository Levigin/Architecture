from ItemGenerator import ItemGenerator
from bronzeReward import BronzeReward


class BronzeGenerator(ItemGenerator):

    def create_item(self, l_border, r_border):
        return BronzeReward(l_border, r_border)
