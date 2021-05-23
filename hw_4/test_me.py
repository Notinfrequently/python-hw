import json
import unittest
from advert import Advert

case_1 = """{
  "title": "iPhone X",
  "price": 100,
  "location": {
    "address": "город Самара, улица Мориса Тореза, 50",
    "metro_stations": ["Спортивная", "Гагаринская"]
  }
}"""

case_2 = """{
  "title": "Вельш-корги",
  "price": 1000,
  "class": "dogs",
  "location": {
    "address": "сельское поселение Ельдигинское,\
       поселок санатория Тишково, 25",
    "more" : {"and_more" : "even_more!"}
  }
}"""


class Test(unittest.TestCase):

    test_case_1 = json.loads(case_1)
    test_case_2 = json.loads(case_2)

    def test_default_repr(self):
        test = Advert(self.test_case_1)
        correct = 'iPhone X | 100 ₽'
        self.assertEqual(correct, str(test))

    def test_keyword_call(self):
        test = Advert(self.test_case_2)
        correct = "dogs"
        self.assertEqual(correct, test.class_)

    def test_price_setter(self):
        test = Advert(self.test_case_1)
        with self.assertRaises(ValueError):
            test.price = -1

    def test_dot_call(self):
        test = Advert(self.test_case_2)
        correct = "even_more!"
        self.assertEqual(correct, test.location.more.and_more)


if __name__ == '__main__':
    unittest.main()
