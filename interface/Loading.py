__metaclass__ = type

from interface.scene import loading_scenes
import time
from PIL import Image
from util.anti import *


class Loading:
    def __init__(self):
        self.scene = []
        self.mark = []

    def have_fun(self):
        im = Image.open(f"./{self.scene}")
        im_size = im.size
        x = im_size[0] / 4
        y = im_size[1] / 4
        # create random action list
        max_act = []
        if self.mark == loading_scenes[1]:
            max_act = 3
        elif self.mark == loading_scenes[0]:
            max_act = 5
        action = []
        press = "tap"
        swipes = "swipe"
        for i in range(5):
            action.append(press)
            action.append(swipes)
        random.shuffle(action)
        # do random actions
        for j in range(random.randrange(1, max_act)):
            if action[j] == press:
                x0 = 2 * x + random.randrange(-x, x)
                y0 = 2 * y + random.randrange(-y, y)
                print("Tap:", self.mark, x0, y0)
                basic_tap(x0, y0)
            if action[j] == swipes:
                time.sleep(0.2)
                x0 = 2 * x + random.randrange(-x, x)
                y0 = 2 * y + random.randrange(-y, y)
                x1 = 2 * x + random.randrange(-x / 2, x / 2)
                y1 = 2 * y + random.randrange(-y / 2, y / 2)
                delay = random.randrange(100, 1000)
                print("Swipe:", self.mark, x0, y0, x1, y1, delay)
                swipe(x0, y0, x1, y1, random.randrange(50, 250))
