import math


class Point(object):
    x: float
    y: float

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f'<{self.x}, {self.y}>'

    def move(self, delta_x: float, delta_y: float) -> None:
        self.x += delta_x
        self.y += delta_y

    @staticmethod
    def distance(punkt1, punkt2):
        return math.sqrt((punkt1.x-punkt2.x) ** 2 + (punkt1.y-punkt2.y) ** 2)
