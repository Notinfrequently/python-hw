import pytest
import funcs

def test_ilen():
    assert funcs.ilen((x for x in range(10))) == 10
    assert funcs.ilen((x for x in range(0))) == 0


def test_flatten():
    assert list(funcs.flatten( [0, [1, [2, 3]]] )) == [0, 1, 2, 3]
    assert list(funcs.flatten([[],[1,2,3]])) == [1,2,3]


def test_distinct():
    assert list(funcs.distinct([1, 2, 0, 1, 3, 0, 2])) == [1, 2, 0, 3]
    assert list(funcs.distinct([])) == []
    assert list(funcs.distinct([1,1,1,1,1])) == [1]


def test_groupby():
    dic_1 = [
        {'gender': 'female', 'age': 33},
        {'gender': 'male', 'age': 20},
        {'gender': 'female', 'age': 21},
    ]
    dic_2 = [{
        'female': [
            {'gender': 'female', 'age': 23},
            {'gender': 'female', 'age': 21},
        ],
        'male': [{'gender': 'male', 'age': 20}] }]
    assert funcs.groupby("gender", dic_1) == {'gender': 'age'}
    assert funcs.groupby("age", dic_2) == {'female': 'male'}


def test_chunks():
    assert list(funcs.chunks(3, [0, 1, 2, 3, 4])) == [[0, 1, 2], [3, 4]]
    assert list(funcs.chunks(0, [0, 1, 2, 3, 4])) == [0, 1, 2, 3, 4]
    with pytest.raises(ValueError):
        list(funcs.chunks(10, [0, 1, 2, 3, 4]))


def test_first():
    assert funcs.first(x for x in range(10)) == 0
    assert funcs.first(x for x in range(0)) == None


def test_last():
    assert funcs.last(x for x in range(10)) == 9
    assert funcs.last(x for x in range(0)) == None
