from lab_python_oop.rectangle import Rectangle

class Square(Rectangle):
    """
    Класс «Квадрат».
    """
    FIGURE_TYPE = "Квадрат"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, side, color):
        self.side = side
        # Передаем ширину и высоту, равные стороне
        super().__init__(side, side, color)

    def __repr__(self):
        return "{} {} цвета со стороной {} площадью {}.".format(
            self.get_figure_type(),
            self._color.color,
            self.side,
            self.area()
        )