from cards.kind import buster_card


def arrange(cards):
    total = 0
    rank = [0, 0, 0]
    # calculate the attack
    for i in range(len(cards)):
        cards[i].priority = 0
        for j in range(len(cards)):
            if j == i:
                continue
            else:
                cards[j].priority = 1
                for k in range(len(cards)):
                    if k == i or k == j:
                        continue
                    else:
                        cards[k].priority = 2
                        orders = [i, j, k]

                        # extra card recognition
                        if cards[i].chain == 1 and \
                                cards[j].chain == 1 and \
                                cards[k].chain == 1:
                            # B B B
                            if cards[i].type == buster_card and \
                                    cards[j].type == buster_card and \
                                    cards[k].type == buster_card:
                                for ordera in orders:
                                    cards[ordera].serial = "bc"
                            # A A A / Q Q Q
                            elif cards[i].type == cards[j].type and \
                                    cards[j].type == cards[k].type:
                                for orderb in orders:
                                    cards[orderb].serial = "aqc"
                            # B A/Q A/Q
                            elif cards[i].type == buster_card and \
                                    cards[j].type != buster_card and \
                                    cards[k].type != buster_card:
                                for orderc in orders:
                                    cards[orderc].serial = "bnc"
                            # A/Q B/A/Q B/A/Q
                            else:
                                for orderd in orders:
                                    cards[orderd].serial = "nc"

                        # normal recognition
                        for order in orders:
                            if cards[i].type == buster_card:
                                cards[order].get_atk(1)
                            else:
                                cards[order].get_atk(0)

                    atk = cards[i].atk + cards[j].atk + cards[k].atk
                    # get the highest attack
                    if atk > total:
                        total = atk
                        rank[0] = i
                        rank[1] = j
                        rank[2] = k
                    # reset the attack index of the cards
                    for l in range(5):
                        cards[l].atk = 1.0
                        cards[l].serial = ""

    print("Order of the cards: ", rank)
    decision = [cards[rank[0]].crd, cards[rank[1]].crd, cards[rank[2]].crd]
    return decision


