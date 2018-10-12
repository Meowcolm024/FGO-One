from util.split import split
from cards.Combat import *


split()
test = Combat()
test.get_arrangement()
for i in range(5):
    print(test.cards[i].servant, test.cards[i].chain, test.cards[i].crd, test.cards[i].mark, test.cards[i].serial)
