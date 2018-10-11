from util.split import split
from extra.matching import matching
from cards.Combat import *
"""
cards = matching()
for i in range(5):
    print(cards[i].servant, cards[i].chain, cards[i].crd, cards[i].mark)
"""
split()
test = Combat()
for i in range(5):
    print(test.cards[i].servant, test.cards[i].chain, test.cards[i].crd, test.cards[i].mark)
for i in range(len(test.servants)):
    print(test.servants[i].count)

out = test.get_arrangement()
print(out)
