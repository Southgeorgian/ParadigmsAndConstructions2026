class FigureColor:
    """
    Класс «Цвет фигуры».
    """
    def __init__(self):
        self._color = None

    @property
    def color(self):
        """Геттер: возвращает цвет."""
        return self._color

    @color.setter
    def color(self, value):
        """Сеттер: устанавливает цвет."""
        self._color = value