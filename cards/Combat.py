from extra.extra import get_extra
from extra.matching import matching
from config import script_mode
from cards.default_mode import arrange

__metaclass__ = type


class Combat:
    def __init__(self):
        self.cards = matching()
        self.servants = get_extra()
        self.modes = script_mode
        self.card_crd = self.get_arrangement()

    def get_arrangement(self):
        if self.modes == "default_mode":
            rank = arrange(self.cards)
            return rank
