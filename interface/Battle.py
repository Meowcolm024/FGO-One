__metaclass__ = type

from cards.decision import arrange
from util.split import split


class Battle:
    def __init__(self):
        self.card_crd = []

    def get_cards(self):
        split()
        rank = arrange()
        self.card_crd = [rank[0], rank[1], rank[2]]

