from lab_python_oop.figure import Figure
from lab_python_oop.color import FigureColor

class Rectangle(Figure):
    """
    Класс «Прямоугольник».
    """
    # Поле данных класса для названия фигуры
    FIGURE_TYPE = "Прямоугольник"

    @classmethod
    def get_figure_type(cls):
        """Метод класса, возвращающий название фигуры."""
        return cls.FIGURE_TYPE

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self._color = FigureColor()  # Создаем объект класса «Цвет фигуры»
        self._color.color = color    # Используем свойство для записи цвета

    def area(self):
        """Переопределенный метод площади."""
        return self.width * self.height

    def __repr__(self):
        """Возвращает строковое представление фигуры."""
        return "{} {} цвета шириной {} и высотой {} площадью {}.".format(
            self.get_figure_type(),
            self._color.color,
            self.width,
            self.height,
            self.area()
        )