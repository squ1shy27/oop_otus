# Прямоугольник
from figure import Figure


class Rectangle(Figure):

    def __init__(self, first_side, second_side):
        if second_side <= 0 or first_side <= 0:
            raise ValueError("side cant be < 0")
        self.first_side = first_side
        self.second_side = second_side


    @property
    def get_perimetr(self):
        return (self.first_side + self.second_side) * 2

    @property
    def get_area(self):
        return self.second_side * self.first_side

rectangle = Rectangle(5, 7)

