# Импорты наших классов
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square

# Импорт внешнего пакета
from colorama import init, Fore, Style


def main():
    # Инициализация colorama
    init(autoreset=True)

    N = 5  # Номер вашего варианта

    # Создаем объекты
    rect = Rectangle(N, N, "синего")
    circle = Circle(N, "зеленого")
    square = Square(N, "красного")

    # Выводим информацию (используя colorama)
    print(Fore.BLUE + str(rect))
    print(Fore.GREEN + str(circle))
    print(Fore.RED + str(square))


if __name__ == "__main__":
    main()