from cards.Cards import *
from util.filter import *
from cards.kind import *
from util.cvs import *


def init():

    a = Card()
    b = Card()
    c = Card()
    d = Card()
    e = Card()
    global cards
    cards = [a, b, c, d, e]


def init_cards():

    card_types = [quick_card, arts_card, buster_card]

    for i in range(5):
        for card_type in card_types:
            sh = f"../temp/{i}.png"
            if check(sh, card_type, 0.9) == 1:
                pos = filter_crd(sh, card_type, 0.9)
                cards[i].crd = pos
