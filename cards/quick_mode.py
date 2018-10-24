from cards.kind import quick_card
from cards.default_mode import arrange


def get_quick(cards):

    quicks = []
    counts = []

    for i in range(5):
        if cards[i].type == quick_card:
            quicks.append(cards[i])
            counts.append(i)

    if len(quicks) <= 2 or len(quicks) == 5:
        rank = arrange(cards)
        return rank
    elif len(quicks) == 3:
        rank = [quicks[0].crd, quicks[1].crd, quicks[2].crd]
        print("Order of the cards: ", counts)
        return rank
    else:
        rank = arrange(quicks)
        return rank

