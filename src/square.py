# Квадрат
# Прямоугольник
from src.figure import Figure
from src.triangle import *
from src.rectangle import Rectangle



class Square(Rectangle):

    def __init__(self, first_side):
        super().__init__(first_side)

        if first_side <= 0:
            raise ValueError("side cant be < 0")

    @property
    def get_perimetr(self):
        return self.first_side * 4

    @property
    def get_area(self):
        return self.first_side * self.first_side

