import os
from phantasms.Phantasms import *
from util.cvs import check
from PIL import Image


def init():
    a = Phantasms()
    b = Phantasms()
    c = Phantasms()

    global nobles
    nobles = [a, b, c]


def match_servants():
    servants = []
    for i in range(5):
        if os.path.exists(f"./temp/servant{i}.png") == 1:
            servants.append(i)

    for j in range(len(servants)):
        nobles[j].servant = servants[j]

    img = Image.open("./temp/np.png")
    img_size = img.size
    gap = (img_size[0] - 1920) / 2
    length = 384  # 1920/5
    exactx = 210
    orgx = gap + length + exactx
    height = img_size[1]
    exacty = height * 2 / 3

    for servant in servants:
        templ = f"./temp/servant{servant}.png"
        for i in range(3):
            img = f"./temp/np{i}.png"
            if check(img, templ, 0.68) == 1:
                x = orgx + i * length
                y = exacty
                nobles[i].crd = [x, y]


def match_np():
    init()
    match_servants()

    for i in range(len(nobles)):
        print("npcrd: ", nobles[i].crd)

    return nobles
