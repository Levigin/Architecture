from ItemGenerator import ItemGenerator
from gemReward import GemReward


class GemsGenerator(ItemGenerator):

    def create_item(self, l_border, r_border):
        return GemReward(l_border, r_border)
