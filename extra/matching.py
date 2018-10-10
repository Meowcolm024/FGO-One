from extra.extra import get_extra
from cards.positioning import positioning


def matching():

    cards = positioning()
    servants = get_extra()

    counts = len(servants)

    for i in range(counts):
        sv_cards = servants[i].count
        for j in sv_cards:
            cards[j].servant = servants[i].order
            if len(sv_cards) >= 3:
                cards[j].chain = 1

    return cards
