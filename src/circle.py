# Круг
import math
from src.figure import Figure
from src.triangle import *
from src.rectangle import *

class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius
    @property
    def get_area(self):
        return math.pi * (self.radius ** 2)


    @property
    def get_perimetr(self):
        return 2 * math.pi * self.radius

circle = Circle(8)
circle.get_area
circle.get_perimetr