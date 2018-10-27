from cards.kind import arts_card
from cards.default_mode import arrange


def get_arts(cards):

    arts = []
    counts = []

    for i in range(5):
        if cards[i].type == arts_card:
            arts.append(cards[i])
            counts.append(i)

    if len(arts) <= 2 or len(arts) == 5:
        rank = arrange(cards)
        return rank
    elif len(arts) == 3:
        rank = [arts[0].crd, arts[1].crd, arts[2].crd]
        print("Order of the cards: ", counts)
        return rank
    else:
        rank = arrange(arts)
        return rank

