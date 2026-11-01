import sys
import math


class BiquadraticEquation:
    """
    Класс для решения биквадратного уравнения
    Ax^4 + Bx^2 + C = 0.
    """

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.d = self.b * self.b - 4.0 * self.a * self.c

    def get_roots(self):
        """
        Вычисляет действительные корни биквадратного уравнения.

        Returns:
            list[float]: Список действительных корней.
        """
        result = []

        if self.d < 0.0:
            return result

        if self.d == 0.0:
            y = -self.b / (2.0 * self.a)

            if y > 0.0:
                root = math.sqrt(y)
                result.append(root)
                result.append(-root)
            elif y == 0.0:
                result.append(0.0)

        else:
            sq_d = math.sqrt(self.d)

            y1 = (-self.b + sq_d) / (2.0 * self.a)
            y2 = (-self.b - sq_d) / (2.0 * self.a)

            if y1 > 0.0:
                root1 = math.sqrt(y1)
                result.append(root1)
                result.append(-root1)
            elif y1 == 0.0:
                result.append(0.0)

            if y2 > 0.0:
                root2 = math.sqrt(y2)
                result.append(root2)
                result.append(-root2)
            elif y2 == 0.0:
                result.append(0.0)

        return result


def get_coef(index, prompt, allow_zero=True):
    """
    Читаем коэффициент из командной строки или вводим с клавиатуры.

    Args:
        index (int): Номер параметра в командной строке.
        prompt (str): Приглашение для ввода коэффициента.
        allow_zero (bool): Разрешено ли значение 0.

    Returns:
        float: Корректный коэффициент.
    """

    # Сначала пробуем получить коэффициент из командной строки
    try:
        coef_str = sys.argv[index]
        coef = float(coef_str)

        if not allow_zero and coef == 0.0:
            raise ValueError

        return coef

    except (IndexError, ValueError):
        # Если параметра нет, он некорректен
        # или коэффициент A равен нулю,
        # вводим коэффициент с клавиатуры

        while True:
            print(prompt)
            coef_str = input()

            try:
                coef = float(coef_str)

                if not allow_zero and coef == 0.0:
                    print("Коэффициент A не должен быть равен нулю.")
                    continue

                return coef

            except ValueError:
                print("Некорректное значение. Повторите ввод.")


def main():
    """
    Основная функция.
    """

    a = get_coef(
        1,
        "Введите коэффициент A:",
        allow_zero=False
    )

    b = get_coef(
        2,
        "Введите коэффициент B:"
    )

    c = get_coef(
        3,
        "Введите коэффициент C:"
    )

    equation = BiquadraticEquation(a, b, c)

    roots = equation.get_roots()

    if len(roots) == 0:
        print("Действительных корней нет.")
    else:
        print("Действительные корни:")
        for root in roots:
            print(root)


if __name__ == "__main__":
    main()