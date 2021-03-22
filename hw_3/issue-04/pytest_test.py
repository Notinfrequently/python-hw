import pytest
import one_hot_encoder


def test_one_city():
    cities = ['Moscow']
    actual = one_hot_encoder.fit_transform(cities)
    expected = [
        ('Moscow', [1])
    ]
    assert actual == expected


def test_nothing():
    with pytest.raises(TypeError):
        one_hot_encoder.fit_transform()


def test_two_citys():
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
    assert actual_1 == expected_1
    assert actual_2 == expected_2


def test_example_from_tast():
    cities = ['Moscow', 'New York', 'Moscow', 'London']
    actual = one_hot_encoder.fit_transform(cities)
    expected = [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
    ]
    assert actual == expected
