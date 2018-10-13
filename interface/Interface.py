import cv2

from cards.Combat import Combat
from interface.Battle import *
from interface.scene import *
from interface.Basic import *
from interface.Support import *
from interface.Finish import *
from interface.Loading import *
from util.cvs import analyze
from util.log import output_log
from config import screenshot_path
from util.split import split

__metaclass__ = type


class Interface:
    def __init__(self):
        self.screenshot = cv2.imread(screenshot_path, 0)
        self.threshold = 0.9
        self.basic_scenes = [cv2.imread(f"./assets/scene/{basic_scene}.png", 0) for basic_scene in basic_scenes]
        self.battle_scenes = [cv2.imread(f"./assets/battle/{battle_scene}.png", 0) for battle_scene in battle_scenes]
        self.support_scene = cv2.imread(f"./assets/scene/{support_scene}.png", 0)
        self.finish_scenes = [cv2.imread(f"./assets/scene/{finish_scene}.png", 0) for finish_scene in finish_scenes]
        self.loading_scenes = [cv2.imread(f"./assets/scene/{loading_scene}.png", 0) for loading_scene in loading_scenes]

    def get_basic(self):
        for basic_scene in self.basic_scenes:
            if analyze(self.screenshot, basic_scene, self.threshold) == 1:
                basic_interface = Basic()
                basic_interface.scene = basic_scene
                basic_interface.sh = self.screenshot
                basic_interface.get_button()
                out = "[BASIC] Buttons: " + str(basic_interface.btn_crd)
                print(out)
                output_log(out)
                return basic_interface.end

    def get_support(self):
        if analyze(self.screenshot, self.support_scene, self.threshold) == 1:
            support_interface = Support()
            support_interface.scene = screenshot_path
            support_interface.select_support()
            out = "[SUPPORT] Position: " + str(support_interface.crd)
            print(out)
            output_log(out)

    def get_finish(self):
        for finish_scene in self.finish_scenes:
            if analyze(self.screenshot, finish_scene, self.threshold) == 1:
                finish_interface = Finish()
                finish_interface.scene = screenshot_path
                finish_interface.pass_finish()

    def get_loading(self):
        for loading_scene in self.loading_scenes:
            if analyze(self.screenshot, loading_scene, self.threshold) == 1:
                loading_interface = Loading()
                loading_interface.scene = screenshot_path
                loading_interface.mark = self.loading_scenes.index(loading_scene)
                loading_interface.have_fun()

    def get_battle(self):
        for battle_scene in self.battle_scenes:
            if analyze(self.screenshot, battle_scene, self.threshold) == 1:
                split()
                combat = Battle()
                combat.get_cards()
                break

    def recognize(self):
        self.get_basic()
        self.get_support()
        self.get_battle()
        self.get_finish()
        self.get_loading()
