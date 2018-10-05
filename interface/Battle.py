__metaclass__ = type

import time
from cards.decision import arrange
from util.split import split
from util.anti import tap_card
import random


class Battle:
    def __init__(self):
        self.card_crd = []

    def get_cards(self):
        split()
        rank = arrange()
        self.card_crd = [rank[0], rank[1], rank[2]]
        for i in range(3):
            tap_card(rank[i][0], rank[i][1])
            time.sleep(random.uniform(0.1, 0.2))
        time.sleep(2.2)
