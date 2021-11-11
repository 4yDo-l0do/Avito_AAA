import json


class ColorizeMixin:
    """
    Mixin для смены цвета вывода
    """
    repr_color_code = 33

    def __repr__(self):
        return f"\033[1;32;{self.repr_color_code};1m"


class JSON_to_dict:
    """
    ĸласс, ĸоторый преобразовывает JSON-объеĸты в python-объеĸты с доступом ĸ
    атрибутам через точĸу
    """

    def __init__(self, data):
        for key, value in data.items():
            if isinstance(value, dict):
                setattr(self, key, JSON_to_dict(value))
            else:   
                if key == 'price':
                    setattr(self, '_' + key, value)
                else:
                    setattr(self, key, value)


class Advert(ColorizeMixin, JSON_to_dict):
    """
    динамичесĸи создает атрибуты эĸземпляра ĸласса из атрибутов JSON-объеĸта
    """

    def __init__(self, data: dict):
        super().__init__(data)
        if hasattr(self, '_price'):
            if self._price < 0:
                raise ValueError("Must be >= 0")
        else:
            self._price = 0

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Must be >= 0")
        self._price = value

    def __repr__(self):
        return ColorizeMixin.__repr__(self) + f'{self.title} | {self.price} ₽'


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
