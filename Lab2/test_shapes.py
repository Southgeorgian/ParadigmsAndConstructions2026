import unittest
import math
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square


class TestShapes(unittest.TestCase):

    def test_rectangle_area(self):
        rect = Rectangle(3, 4, "синий")
        # Площадь прямоугольника 3 на 4 = 12
        self.assertEqual(rect.area(), 12)

        def test_circle_area(self):
            circle = Circle(2, "зеленый")
            # Считаем точное ожидаемое значение: pi * r^2
            expected_area = math.pi * (2 ** 2)

            # Проверяем с точностью до 7 знаков (по умолчанию в assertAlmostEqual 7)
            self.assertAlmostEqual(circle.area(), expected_area)

    def test_square_area(self):
        square = Square(5, "красный")
        # Площадь квадрата 5*5 = 25
        self.assertEqual(square.area(), 25)

    def test_square_inherits_rectangle_type(self):
        square = Square(5, "красный")
        # Проверяем, что название возвращается правильное
        self.assertEqual(square.get_figure_type(), "Квадрат")


if __name__ == '__main__':
    unittest.main()