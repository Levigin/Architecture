from HW2.gameItem import GameItem
import random


class PlatinumReward(GameItem):

    def open_item(self):
        random_amount = random.randrange(self.l_border, self.r_border + 1)
        print(f'{random_amount} platinum!')
