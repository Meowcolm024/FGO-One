from cards.positioning import *


def arrange():

    cards = positioning()
    total = 0
    rank = [0, 0, 0]

    for i in range(5):
        cards[i].priority = 0
        for j in range(5):
            if j == i:
                continue
            else:
                cards[j].priority = 1
                for k in range(5):
                    if k == i or k == j:
                        continue
                    else:
                        cards[k].priority = 2
                        orders = [i, j, k]
                        for order in orders:
                            if cards[i].type == buster_card:
                                cards[order].get_atk(1)
                            else:
                                cards[order].get_atk(0)

                    atk = cards[i].atk + cards[j].atk + cards[k].atk

                    if atk > total:
                        total = atk
                        rank[0] = i
                        rank[1] = j
                        rank[2] = k

    print(rank)
    decision = [cards[rank[0]].crd, cards[rank[1]].crd, cards[rank[2]].crd]
    return decision


