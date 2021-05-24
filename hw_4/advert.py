import keyword
import json


class ColorizeMixin:

    r_color = '\033[33m'
    b_color = '\033[0m'

    def __repr__(self):
        return f"{self.r_color}{self.title} \
            | {self.price} ₽{self.b_color}"


class Advert(ColorizeMixin):
    _price = 0

    def __init__(self, data: dict):
        self._set_atrs(data)

    def __repr__(self):
        return f'{self.title} | {self.price} ₽'

    def __setattr__(self, key, value):
        if keyword.iskeyword(key):
            key = key + "_"
        super.__setattr__(self, key, value)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price: int):
        if price < 0:
            raise ValueError("ValueError: must be >= 0")
        self._price = price

    def _set_atrs(self, atrs):
        for key, value in atrs.items():
            if isinstance(value, dict):
                new_obj = self._make_object(key, value)
                self.__setattr__(key, new_obj)
            else:
                self.__setattr__(key, value)

    def _make_object(self, name, attribute: dict):
        for key, value in attribute.items():
            if isinstance(value, dict):
                attribute[key] = self._make_object(key, value)
        return type(name, (object, ), attribute)


lesson_str = """{
  "title": "Вельш-корги",
  "price": 1000,
  "class": "dogs",
  "location": {
    "address": "сельское поселение Ельдигинское,\
         поселок санатория Тишково, 25",
    "more" : {
        "and_more" : "even_more!"
        }
  }
}"""