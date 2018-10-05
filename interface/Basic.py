__metaclass__ = type

from util.filter import filter_crd
from util.anti import basic_tap
from util.cvs import check


class Basic:

    def __init__(self):
        self.scene = []
        self.sh = []
        self.btn_crd = [0, 0]
        self.end = []

    def get_button(self):
        position = filter_crd(self.sh, self.scene, 0.9)
        self.btn_crd[0] = position[0][0]
        self.btn_crd[1] = position[0][1]
        basic_tap(self.btn_crd[0], self.btn_crd[1])

        if check(self.sh, self.scene, 0.9) == 1:
            self.end = "end"
