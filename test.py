from cards.decision import *
from util.split import *


split()
cards = positioning()
print('-------------')
for num in range(5):
    print(f"Card({num}): ", cards[num].crd, cards[num].mark, cards[num].type)
print('-------------')
rank = arrange()
print('-------------')
print("Coordinates of selected cards: ", rank)
