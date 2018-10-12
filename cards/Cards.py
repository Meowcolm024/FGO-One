__metaclass__ = type
from cards.attack import *
from cards.kind import *


class Card:
    def __init__(self):
        self.crd = []
        self.mark = ""
        self.type = ""
        self.priority = []
        self.atk = 1.0
        self.chain = 0
        self.servant = []
        self.serial = ""

    def get_atk(self, ex):
        # attack from type of the card
        if self.type == quick_card:
            self.atk = self.atk * quick
        elif self.type == arts_card:
            self.atk = self.atk * arts
        elif self.type == buster_card:
            self.atk = self.atk * buster

        # attack from card order
        if self.priority == 0:
            self.atk = self.atk * zero
        elif self.priority == 1:
            self.atk = self.atk * first
        elif self.priority == 2:
            self.atk = self.atk * second

        # attack from buster benefit
        if ex == 1:
            self.atk = self.atk + exbst

        # attack from extra card
        if self.serial == "bc":
            self.atk = self.atk + 5.2
        if self.serial == "aqc":
            self.atk = self.atk + 3.5
        if self.serial == "bnc":
            self.atk = self.atk + 3
        if self.serial == "nc":
            self.atk = self.atk + 2

        # attack from mark of the card
        if self.mark == restraint_mark:
            self.atk = self.atk * restraint
        elif self.mark == resistance_mark:
            self.atk = self.atk * resistance

