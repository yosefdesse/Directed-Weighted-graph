import math

n = 0


class Node:

    def __init__(self, key, pos: tuple = None, info: str = ""):
        self.key = key
        self.tag = -1
        self.path = list()
        self.weight = 0
        self.distance = math.inf
        self.info = info
        self.previous = -1
        self.pos = pos
        self.edges = dict()
        self.back_edges = dict()

    def get_key(self):
        return self.key

    def _gt_(self, other):
        return self.distance > other.distance

    def get_tag(self):
        return self.tag

    def set_tag(self, tag):
        self.tag = tag

    def get_info(self):
        return self.info

    def set_info(self, info):
        self.info = info

    def get_pos(self):
        return self.pos

    def set_pos(self, x: float, y: float, z: float):

        self.pos = [x, y, z]

    def set_distance(self, distance):
        self.distance = distance

    def get_distance(self):
        return self.distance

    def get_prev(self):
        return self.previous

    def set_prev(self, prev):
        self.previous = prev

    def _repr_(self) -> str:
        return f"{self.key}"