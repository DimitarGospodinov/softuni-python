import math
from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_x(self, new_x):
        self.x = new_x

    def set_y(self, new_y):
        self.y = new_y

    def distance(self, x2, y2):
        r = math.sqrt((x2 - self.x) ** 2 + (y2 - self.y) ** 2)
        return r


p = Point(2, 4)
p.set_x(3)
p.set_y(5)
print(p.distance(10, 2))
