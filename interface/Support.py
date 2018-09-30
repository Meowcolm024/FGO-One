__metaclass__ = type

import random
from PIL import Image


class Support:
    def __init__(self):
        self.crd = []

    def select_support(self, sh):
        im = Image.open(f"./{sh}")
        im_size = im.size

        x = random.randrange(-300, 300) + (im_size[0] / 2)
        y = random.randrange(-200, 200) + (im_size[1] / 2)

        self.crd = [x, y]

