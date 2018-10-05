__metaclass__ = type

import random
from PIL import Image
from util.anti import basic_tap


class Support:
    def __init__(self):
        self.scene = []
        self.crd = []

    def select_support(self):
        im = Image.open(f"./{self.scene}")
        im_size = im.size

        x = random.randrange(-300, 300) + (im_size[0] / 2)
        y = random.randrange(-200, 200) + (im_size[1] / 2)

        self.crd = [x, y]
        basic_tap(self.crd[0], self.crd[1])
