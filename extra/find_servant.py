from util.cvs import check
from extra.Servant import *
import os
from PIL import Image


def init():
    a = Servant()
    b = Servant()
    c = Servant()

    global servants
    servants = [a, b, c]


def check_exists():
    ses = []
    for i in range(5):
        if os.path.exists(f"./temp/servant{i}.png") == 1:
            ses.append(i)
    print("ses:", ses)
    return ses


def get_exists():
    exists = [i for i in range(5)]
    # filter same servants
    for exist in exists:
        tmp = f"./temp/s{exist}.png"
        for exis in exists:
            if exist != exis:
                pic = f"./temp/{exis}.png"
                if check(pic, tmp, 0.9) == 1:
                    exists.remove(exis)
    for i in exists:
        im = Image.open(f"./temp/s{i}.png")
        im.save(f"./temp/servant{i}.png")

    return exists


def decide():
    existed = check_exists()

    if len(existed) == 0:
        exists = get_exists()
        existed = exists
    elif len(existed) == 3:
        existed = existed
    elif len(existed) < 3:
        exists = [i for i in range(5)]
        existss = [i for i in range(5)]
        for exist in existed:
            for exis in exists:
                tmp = f"./temp/s{exist}.png"
                pic = f"./temp/{exis}.png"
                if check(pic, tmp, 0.9) == 1:
                    existss.remove(exis)

        for existe in existss:
            tmp = f"./temp/s{existe}.png"
            for exise in existss:
                if existe != exise:
                    pic = f"./temp/{exise}.png"
                    if check(pic, tmp, 0.9) == 1:
                        existss.remove(exise)

        for i in existss:
            im = Image.open(f"./temp/s{i}.png")
            im.save(f"./temp/servant{i}.png")

        existed = existed + existss

    print(existed)
    return existed


def init_extra():
    exists = decide()
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
