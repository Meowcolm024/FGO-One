"""detect servants"""
from util.cvs import check
from extra.Servant import *


def init():
    a = Servant()
    b = Servant()
    c = Servant()

    global servants
    servants = [a, b, c]


def init_extra():
    exists = [i for i in range(5)]
    # filter same servants
    for exist in exists:
        tmp = f"./temp/s{exist}.png"
        for exis in exists:
            if exist != exis:
                pic = f"./temp/{exis}.png"
                if check(pic, tmp, 0.9) == 1:
                    exists.remove(exis)

    counts = [i for i in range(len(exists))]
    for count in counts:
        servants[count].order = exists[count]
    # mark servants
    for coun in counts:
        stmp = f"./temp/s{servants[coun].order}.png"
        for k in range(5):
            spic = f"./temp/{k}.png"
            if check(spic, stmp, 0.9) == 1:
                servants[coun].count.append(k)


def get_extra():
    init()
    init_extra()
    return servants
