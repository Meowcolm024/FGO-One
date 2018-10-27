from extra.extra import get_extra
from extra.matching import matching
from config import script_mode
from cards.default_mode import arrange
from cards.quick_mode import get_quick
from cards.arts_mode import get_arts
from phantasms.detection import match_np
from phantasms.turns import get_turns

__metaclass__ = type


class Combat:
    def __init__(self):
        self.cards = matching()
        self.servants = get_extra()
        self.modes = script_mode
        self.turns = get_turns()
        self.card_crd = self.get_np()

    def get_np(self):
        if not self.turns:
            return self.get_arrangement()
        a = self.turns[0]
        if len(self.turns) == 3:
            b = self.turns[2]
        else:
            b = self.turns[1]
        npcrd = []
        if float(a) / float(b) == 1:
            nps = match_np()
            if len(nps) == 0:
                return self.get_arrangement()
            else:
                for i in range(len(nps)):
                    if nps[i].crd:
                        npcrd.append(nps[i].crd)
                npcrd = npcrd + self.get_arrangement()
            return npcrd
        else:
            return self.get_arrangement()

    def get_arrangement(self):
        if self.modes == "default_mode":
            rank = arrange(self.cards)
            return rank
        if self.modes == "quick_mode":
            rank = get_quick(self.cards)
            return rank
        if self.modes == "arts_mode":
            rank = get_arts(self.cards)
            return rank

