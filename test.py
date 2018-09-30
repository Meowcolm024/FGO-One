from cards.positioning import *
from cards.decision import *
from util.split import *


split()
cards = positioning()
num = 3
print(cards[num].crd, cards[num].mark, cards[num].type)
rank = arrange()
print(rank)
