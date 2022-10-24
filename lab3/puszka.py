import math


class SodaCan(object):
    height: int
    radius: int

    def __init__(self, height: int, radius: int):
        self.height = height
        self.radius = radius

    def get_surface_area(self):
        return math.pi*self.radius*(self.height+self.radius)

    def get_volume(self):
        return math.pi*self.radius**2*self.height

