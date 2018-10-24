__metaclass__ = type

import time
from PIL import Image
from util.anti import *
from util.log import output_log


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
        if self.mark == 1:
            max_act = 2
        elif self.mark == 0:
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
                y0 = 2 * y + random.randrange(-y, y - 100)
                out = "[LOADING] Tap: [" + str(self.mark) + "] " + str(x0) + " " + str(y0)
                print(out)
                output_log(out)
                basic_tap(x0, y0)
            if action[j] == swipes:
                time.sleep(0.1)
                x0 = 2 * x + random.randrange(-x, x)
                y0 = 2 * y + random.randrange(-y, y)
                x1 = 2 * x + random.randrange(-x / 3, x / 3)
                y1 = 2 * y + random.randrange(-y / 3, y / 3)
                delay = random.randrange(100, 1000)
                out = "[LOADING] Swipe: [" + str(self.mark) + "] " + str(x0) + " " + str(y0) + " " +\
                      str(x1) + " " + str(y1) + " " + str(delay)
                print(out)
                output_log(out)
                swipe(x0, y0, x1, y1, random.randrange(50, 500))
