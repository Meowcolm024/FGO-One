from cards.Combat import Combat
import time
from util.anti import tap_card
import random


class Battle(Combat):
    def get_cards(self):
        rank = [self.card_crd[0], self.card_crd[1], self.card_crd[2]]
        print(rank)
        for i in range(3):
            tap_card(rank[i][0], rank[i][1])
            time.sleep(random.uniform(0.1, 0.2))
        time.sleep(3)
