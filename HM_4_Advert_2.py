import json
from keyword import iskeyword


class ColorizeMixin:
    """
    Mixin для смены цвета вывода
    """
    repr_color_code = 33

    def __repr__(self):
        text = super().__repr__()
        return f"\033[1;32;{self.repr_color_code};1m{text}"


class JsonToDict:
    """
    ĸласс, ĸоторый преобразовывает JSON-объеĸты в python-объеĸты с доступом ĸ
    атрибутам через точĸу
    """

    def __init__(self, data):
        for key, value in data.items():
            if iskeyword(key):
                key += '_'
            if isinstance(value, dict):
                value = JsonToDict(value)
            setattr(self, key, value)


class BaseAdvert:
    """
    вспомогательный класс для Advert
    """
    def __repr__(self):
        return f'{self.title} | {self.price} ₽'


class Advert(ColorizeMixin, JsonToDict, BaseAdvert):
    """
    динамичесĸи создает атрибуты эĸземпляра ĸласса из атрибутов JSON-объеĸта
    """

    def __init__(self, data: dict):
        if 'price' in data:
            self.price = data.pop('price')
        else:
            self.price = 0
        super().__init__(data)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Must be >= 0")
        self._price = value


if __name__ == "__main__":
    lesson_str = """{
        "title": "python",
        "price": 0,
        "location": {
            "address": "город Москва, Лесная, 7",
            "metro_stations": ["Белорусская"]
            }
        }"""
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    print(lesson_ad.location.address)

    lesson_str = '''{
        "title": "Вельш-корги",
        "price": 1000,
        "class": "dogs",
        "location": {
            "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
            }
        }'''
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    print(lesson_ad)
