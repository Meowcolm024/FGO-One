__metaclass__ = type

from util.cvs import check
from util.log import output_log
from interface.scene import finish_scenes
from PIL import Image
import random
from util.anti import basic_tap


class Finish:
    def __init__(self):
        self.scene = []
        self.crd = []

    def pass_finish(self):
        for finish_scene in finish_scenes:
            scene_path = f"./assets/scene/{finish_scene}.png"
            if check(self.scene, scene_path, 0.9) == 1:
                im = Image.open(f"./{self.scene}")
                im_size = im.size
                x0 = im_size[0] / 4
                y0 = im_size[0] / 4
                x = random.randrange(-x0, x0) + (im_size[0] / 2)
                y = random.randrange(-y0, y0) + (im_size[1] / 2)

                self.crd = [x, y]
                out = "[FINISH] Checked: " + str(finish_scene) + str(x) + str(y)
                print(out)
                output_log(out)
                basic_tap(self.crd[0], self.crd[1])
