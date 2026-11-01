from abc import ABC, abstractmethod

class Figure(ABC):
    """
    Абстрактный класс «Геометрическая фигура».
    """
    @abstractmethod
    def area(self):
        """
        Абстрактный метод для вычисления площади фигуры.
        """
        pass