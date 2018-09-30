# avoid the ID being banned
from util.ats import *
import random


def long_tap(x, y):  # random length tap
    delay = random.randrange(5, 200)
    swipe(x, y, x, y, delay)


def tap_card(x, y):  # tap on random location of the card
    x0 = x + random.uniform(0, 100)
    y0 = y + random.uniform(-150, 0)
    x0 = int(x0)
    y0 = int(y0)
    tap(x0, y0)


def basic_tap(x, y):  # tap on random location of the button
    x0 = x + random.uniform(-25, 25)
    y0 = y + random.uniform(-25, 25)
    x0 = int(x0)
    y0 = int(y0)
    tap(x0, y0)
