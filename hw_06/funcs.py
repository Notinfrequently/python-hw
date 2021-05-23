from typing import Iterable


def ilen(iterable: Iterable):
    """
    >>> foo = (x for x in range(10))
    >>> ilen(foo)
    10
    """
    return len(list(iterable))


print(ilen(range(10)))



def flatten(iterable: Iterable):
    """
    >>> list(flatten([0, [1, [2, 3]]]))
    [0, 1, 2, 3]
    """
    ls = list(iterable)
    if not ls: return ls
    if isinstance(ls[0], list):
        return flatten(ls[0]) + flatten(ls[1:])
    return ls[:1] + flatten(ls[1:])

print(flatten([0, [1, [2, 3]]]))

def distinct(iterable: Iterable):
    """
    >>> list(distinct([1, 2, 0, 1, 3, 0, 2]))
    [1, 2, 0, 3]
    """
    #dicts are insertion ordered 
    return list(dict.fromkeys(iterable))


print(distinct([1, 2, 0, 1, 3, 0, 2]))


def groupby(key, iterable: Iterable):
    """
    >>> users = [
        {'gender': 'female', 'age': 33},
        {'gender': 'male', 'age': 20},
        {'gender': 'female', 'age': 21},
    ]
    >>> groupby('gender', users)
    {
        'female': [
            {'gender': 'female', 'age': 23},
            {'gender': 'female', 'age': 21},
        ],
        'male': [{'gender': 'male', 'age': 20}],
    }
    # Или так:
    >>> groupby('age', users)
    """
    # [x for x in seq if not (x in seen or seen_add(x))]
    # Вау!
    output_iterable = {}
    return {key:val for key, val in iterable if (key, val in output_iterable or output_iterable.update({key:val}))}


users = [
    {'gender': 'female', 'age': 33},
    {'gender': 'male', 'age': 20}, 
    {'gender': 'female', 'age': 21},
]

print(groupby('gender', users))

def chunks(size: int, iterable: Iterable):
    """
    >>> list(chunks(3, [0, 1, 2, 3, 4]))
    [(0, 1, 2), (3, 4, )]
    """
    ls = list(iterable)
    return [ls[i:i + size] for i in range(0, ilen(iterable), size)]

print(list(chunks(3, [0, 1, 2, 3, 4])))


def first(iterable: Iterable):
    """
    >>> foo = (x for x in range(10))
    >>> first(foo)
    0
    >>> first(range(0))
    None
    """
    return next(iterable, None)

foo = (x for x in range(0))
print(first(foo))

def last(iterable: Iterable):
    """
    >>> foo = (x for x in range(10))
    >>> last(foo)
    9
    >>> last(range(0))
    None
    """
    hey = None
    for hey in iterable: pass
    return hey


foo = (x for x in range(10))
print(last(foo))