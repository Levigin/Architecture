import random

from goldGenerator import GoldGenerator
from gemsGenerator import GemsGenerator
from bronzeGenerator import BronzeGenerator
from copperGenerator import CopperGenerator
from ironGenerator import IronGenerator
from lumberGenerator import LumberGenerator
from platinumGenerator import PlatinumGenerator
from silverGenerator import SilverGenerator
from stoneGenerator import StoneGenerator
from sulfurGenerator import SulfurGenerator


generator_list = []


def create_generators(l_border, r_border):
    generator_list.append(GoldGenerator(l_border, r_border))
    generator_list.append(GemsGenerator(l_border, r_border))
    generator_list.append(BronzeGenerator(l_border, r_border))
    generator_list.append(CopperGenerator(l_border, r_border))
    generator_list.append(IronGenerator(l_border, r_border))
    generator_list.append(LumberGenerator(l_border, r_border))
    generator_list.append(PlatinumGenerator(l_border, r_border))
    generator_list.append(SilverGenerator(l_border, r_border))
    generator_list.append(StoneGenerator(l_border, r_border))
    generator_list.append(SulfurGenerator(l_border, r_border))


create_generators(1, 100)

for i in range(100):
    k = random.randrange(0, 10)
    generator_list[k].open_reward()
