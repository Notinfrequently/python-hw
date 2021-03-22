import unittest
import one_hot_encoder


class Tester(unittest.TestCase):
    def test_one_city(self):
        cities = ['Moscow']
        actual = one_hot_encoder.fit_transform(cities)
        expected = [
            ('Moscow', [1])
        ]
        self.assertEqual(actual, expected)
        self.assertNotIn(('Moscow', [1, 0]), actual)
        self.assertNotIn(('Moscow', [0, 1]), actual)
        self.assertNotIn(('Moscow', [1, 1]), actual)

    def test_nothing(self):
        with self.assertRaises(TypeError):
            one_hot_encoder.fit_transform()

    def test_two_citys(self):
        cities_1 = ['Moscow', 'Perm']
        cities_2 = ['Moscow', 'Moscow']
        actual_1 = one_hot_encoder.fit_transform(cities_1)
        actual_2 = one_hot_encoder.fit_transform(cities_2)
        expected_1 = [
            ('Moscow', [0, 1]),
            ('Perm', [1, 0]),
        ]
        expected_2 = [
            ('Moscow', [1]),
            ('Moscow', [1]),
        ]
        self.assertEqual(actual_1, expected_1)
        self.assertEqual(actual_2, expected_2)

    def test_example_from_tast(self):
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        actual = one_hot_encoder.fit_transform(cities)
        expected = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]
        self.assertEqual(actual, expected)
