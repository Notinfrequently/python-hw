from time import sleep, time
from random import random
import string
import re


def calc_duration(func):
    def decorated(*args, **kwargs):
        start_time = time()
        result_func = func(*args, **kwargs)
        end_time = time()
        print(f"Executing took: {end_time-start_time}.")
        return result_func
    return decorated


@calc_duration
def long_executing_task():
    for index in range(3):
        print(f'Iteration {index + 1}')
        sleep(random())


def suppress_errors(errors):
    def decorator(func):
        def decorated(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except errors as e:
                print(f"Problem with: {e}")
        return decorated
    return decorator


@suppress_errors((
    KeyError,
    ValueError,
))
def potentially_unsafe_func(key: str):
    print(f'Get data by the key {key}')
    data = {'name': 'test', 'age': 30}
    return data[key]

print(potentially_unsafe_func('name'))  # everything is ok
print(potentially_unsafe_func('last_name')) 

def result_between(value_min, value_max):
    def decorator(func):
        def decorated(*args, **kwargs):
            result = func(*args, **kwargs)
            if not (value_min <= result <= value_max):
                raise ValueError                
        return decorated
    return decorator


def len_more_than(s_len):
    def decorator(func):
        def decorated(*args, **kwargs):
            result_func = func(*args, **kwargs)
            if (len(result_func) < s_len):
                raise ValueError
        return decorated
    return decorator


@result_between(0, 10)
def sum_of_values(numbers):
    return sum(numbers)


@len_more_than(10)
def show_message(message: str) -> str:
    return f'{message}'

#sum_of_values((1, 3))  # ValueError
#show_message('123456789')  # ValueError

def replace_commas(func):
    def decorated(*args, **kwargs):
        result_func = func(*args, **kwargs)
        return re.sub(r'[^\s\w]', " ", result_func)
    return decorated

def words_title(func):
    def decorated(*args, **kwargs):
        result_func = func(*args, **kwargs)
        def AaA(s):
            s = s.group(1)
            if len(s) == 1:
                return " " + s
            return " " + s[0].upper() + s[1:len(s) - 1] + s[-1].upper()
        return (re.sub(r"(?:\s+)([A-Za-z0-9]+)(?=\s+)", AaA, result_func)).strip()
        #return " ".join(list(map(AaA, result_func.split())))
    return decorated

@words_title
@replace_commas
def process_text(text: str) -> str:
    return text.replace(':', ',')

@replace_commas
@words_title
def another_process(text: str) -> str:
    return text.replace(':', ',')

print(process_text('the French revolution resulted in 3 concepts: freedom,equality,fraternity')) 
print(another_process('the French revolution resulted in 3 concepts: freedom,equality,fraternity'))


def cache_result():
    _cache = {}

    def decorator(func):
        def decorated(*args, **kwargs):
            if args not in _cache:
                _cache[args] = func(*args, **kwargs)
            return _cache[args]
        return decorated
    return decorator


@cache_result()
def some_func(last_name, first_name, age):
    return f'Hi {last_name} {first_name}, you are {age} years old'
