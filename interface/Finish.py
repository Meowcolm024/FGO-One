__metaclass__ = type

from util.cvs import check
from interface.scene import finish_scenes


class Finish:
    def __init__(self):
        self.scene = []
        self.crd = []

    def pass_finish(self):
        for finish_scene in finish_scenes:
            scene_path = f"./assets/scene/{finish_scene}.png"
            if check(self.scene, scene_path, 0.9) == 1:
                print("checked")



