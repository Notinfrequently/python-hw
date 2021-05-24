from typing import Iterable

def ilen(iterable: Iterable):
    """
    >>> foo = (x for x in range(10))
    >>> ilen(foo)
    10
    """
    return len(list(iterable))


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


def distinct(iterable: Iterable):
    """
    >>> list(distinct([1, 2, 0, 1, 3, 0, 2]))
    [1, 2, 0, 3]
    """
    #dicts are insertion ordered 
    return list(dict.fromkeys(iterable))


def groupby(key, iterable: Iterable):
    """
    >>> groupby('gender', [
    ... {'gender': 'female', 'age': 33},
    ... {'gender': 'male', 'age': 20}, 
    ... {'gender': 'female', 'age': 21}, ])
    {'gender': 'age'}
    """
    # [x for x in seq if not (x in seen or seen_add(x))]
    # Вау!
    output_iterable = {}
    return {key:val for key, val in iterable if\
        (key, val in output_iterable or output_iterable.update({key:val}))}


def chunks(size: int, iterable: Iterable):
    """
    >>> list(chunks(3, [0, 1, 2, 3, 4]))
    [[0, 1, 2], [3, 4]]
    """
    if size == 0: return list(iterable)
    elif size > ilen(iterable): raise ValueError
    ls = list(iterable)
    return [ls[i:i + size] for i in range(0, ilen(iterable), size)]


def first(iterable: Iterable):
    """
    >>> print(first(x for x in range(10)))
    0
    >>> print(first(x for x in range(0)))
    None
    """
    return next(iterable, None)


def last(iterable: Iterable):
    """
    >>> last(x for x in range(10))
    9
    >>> print(last(range(0)))
    None
    """
    hey = None
    for hey in iterable: pass
    return hey
