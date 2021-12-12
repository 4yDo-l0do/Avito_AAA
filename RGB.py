from abc import ABC, abstractmethod


class ComputerColor(ABC):
    """Абстрактный класс для создания классов по типу Color"""

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def __mul__(self, other):
        pass

    @abstractmethod
    def __rmul__(self, other):
        pass


class Color(ComputerColor):
    """
    Класс, который выводит ● в заданном цвете RGB и имеет возможность сравнивать, смешивать цвета и уменьшать
    контрастность цвета
    """
    END = '\033[0'
    START = '\033[1;38;2'
    MOD = 'm'

    def __init__(self, r, g, b):
        self.r = r
        self.b = b
        self.g = g

    def __str__(self):
        return f'{self.START};{self.r};{self.g};{self.b}{self.MOD}●{self.END}{self.MOD}'

    __repr__ = __str__

    def __eq__(self, other):
        return isinstance(other, Color) and self.r == other.r and self.b == other.b and self.g == other.g

    def __add__(self, other):
        if isinstance(other, Color):
            return Color(min(self.r + other.r, 255), min(self.b + other.b, 255), min(self.g + other.g, 255))
        else:
            raise ValueError(f"Сложение цвета с {type(other)} недопустимо")

    def __hash__(self):
        return hash((self.r, self.b, self.g))

    def __mul__(self, other):
        if other > 1 or other < 0:
            raise ValueError(f"число должно быть от 0 до 1")
        cl = -256 * (1 - other)
        f = 259 * (cl + 255) / (255 * (259 - cl))
        r = int(f * (self.r - 128) + 128)
        g = int(f * (self.g - 128) + 128)
        b = int(f * (self.b - 128) + 128)

        return Color(r, g, b)

    __rmul__ = __mul__


def print_a(color: ComputerColor):
    """ функция, которая выводит букву А в определенном цвете """
    bg_color = 0.2 * color
    a_matrix = [
        [bg_color] * 19,
        [bg_color] * 9 + [color] + [bg_color] * 9,
        [bg_color] * 8 + [color] * 3 + [bg_color] * 8,
        [bg_color] * 7 + [color] * 2 + [bg_color] + [color] * 2 + [bg_color] * 7,
        [bg_color] * 6 + [color] * 2 + [bg_color] * 3 + [color] * 2 + [bg_color] * 6,
        [bg_color] * 5 + [color] * 9 + [bg_color] * 5,
        [bg_color] * 4 + [color] * 2 + [bg_color] * 7 + [color] * 2 + [bg_color] * 4,
        [bg_color] * 3 + [color] * 2 + [bg_color] * 9 + [color] * 2 + [bg_color] * 3,
        [bg_color] * 19,
    ]

    for row in a_matrix:
        print(''.join(str(ptr) for ptr in row))


if __name__ == '__main__':
    orange1 = Color(255, 165, 0)
    red = Color(255, 0, 0)
    green = Color(0, 255, 0)
    orange2 = Color(255, 165, 0)
    color_list = [orange1, red, green, orange2]
    print(set(color_list))
    print_a(green)
