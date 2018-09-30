__metaclass__ = type
from cards.attack import *


class Card:
    def __init__(self):
        self.crd = []
        self.mark = []
        self.type = []
        self.priority = []
        self.atk = 1

    def get_atk(self, ex):

        # attack from mark of the card
        if self.mark == "restraint":
            self.atk = self.atk * restraint
        elif self.mark == "resistance":
            self.atk = self.atk * resistance

        # attack from type of the card
        if self.type == "quick":
            self.atk = self.atk * quick
        elif self.type == "arts":
            self.atk = self.atk * arts
        elif self.type == "buster":
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
