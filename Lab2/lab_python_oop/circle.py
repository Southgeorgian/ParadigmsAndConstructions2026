import math
from lab_python_oop.figure import Figure
from lab_python_oop.color import FigureColor

class Circle(Figure):
    """
    Класс «Круг».
    """
    FIGURE_TYPE = "Круг"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, radius, color):
        self.radius = radius
        self._color = FigureColor()
        self._color.color = color

    def area(self):
        """Площадь круга: pi * r^2."""
        return math.pi * (self.radius ** 2)

    def __repr__(self):
        return "{} {} цвета радиусом {} площадью {:.2f}.".format(
            self.get_figure_type(),
            self._color.color,
            self.radius,
            self.area()
        )