import sys
import math


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


def get_roots(a, b, c):
    """
    Вычисление действительных корней биквадратного уравнения.
    """

    result = []

    d = b * b - 4.0 * a * c


    if d < 0.0:
        return result

    if d == 0.0:
        y = -b / (2.0 * a)

        if y > 0.0:
            root = math.sqrt(y)
            result.append(root)
            result.append(-root)

        elif y == 0.0:
            result.append(0.0)

    else:
        sq_d = math.sqrt(d)

        y1 = (-b + sq_d) / (2.0 * a)
        y2 = (-b - sq_d) / (2.0 * a)

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

    roots = get_roots(a, b, c)

    if len(roots) == 0:
        print("Действительных корней нет.")
    else:
        print("Действительные корни:")
        for root in roots:
            print(root)


if __name__ == "__main__":
    main()