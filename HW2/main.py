import random

from goldGenerator import GoldGenerator
from gemsGenerator import GemsGenerator

generator_list = []


def create_generators(l_border, r_border):
    generator_list.append(GoldGenerator(l_border, r_border))
    generator_list.append(GemsGenerator(l_border, r_border))


create_generators(1, 100)

for i in range(10):
    k = random.randrange(0, 2)

    generator_list[k].open_reward()
