from cards.Cards import *
from cards.kind import *
from config import screenshot_path
from util.filter import *
from util.cvs import *
from PIL import Image


def init():

    a = Card()
    b = Card()
    c = Card()
    d = Card()
    e = Card()
    global cards
    cards = [a, b, c, d, e]


def init_cards():

    im = Image.open(screenshot_path)
    img_size = im.size
    gap = (img_size[0] - 1920) / 2

    card_types = [quick_card, arts_card, buster_card]
    mark_types = [resistance_mark, restraint_mark]

    for i in range(5):
        # get coordinates
        for card_type in card_types:
            sh = f"./temp/{i}.png"
            tmpl = f"./assets/battle/{card_type}.png"
            if check(sh, tmpl, 0.9) == 1:
                pos = filter_crd(sh, tmpl, 0.9)
                x = pos[0][0] + gap
                y = pos[0][1] + (img_size[1] / 2) - 100
                cards[i].crd = [x, y]
                cards[i].type = card_type
        # get marks
        for mark_type in mark_types:
            sh = f"./temp/{i}.png"
            tmpl = f"./assets/battle/{mark_type}.png"
            if check(sh, tmpl, 0.9) == 1:
                cards[i].mark = mark_type


def positioning():
    init()
    init_cards()
    print(cards[0].crd, cards[0].mark, cards[0].type)

