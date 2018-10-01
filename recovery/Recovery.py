__metaclass__ = type

from util.filter import filter_crd
from util.cvs import check
from recovery.panel import *


class Recovery:
    def __init__(self):
        self.scene = []
        self.crd = [0, 0]
        self.done = 0

    def recover(self):
        apple_path = f"./assets/scene/{apple}.png"
        decide_path = f"./assets/scene/{decide}.png"
        if check(self.scene, apple_path, 0.9) == 1:
            position = filter_crd(self.scene, apple_path, 0.9)
            self.crd[0] = position[0][0]
            self.crd[1] = position[0][1]
            print("Apple: ", self.crd[0], self.crd[1])
            self.done = 1
        if check(self.scene, decide_path, 0.9) == 1:
            position = filter_crd(self.scene, decide_path, 0.9)
            self.crd[0] = position[0][0]
            self.crd[1] = position[0][1]
            print("Decide: ", self.crd[0], self.crd[1])
            self.done = 2

