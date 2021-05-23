from time import sleep, time
from random import random
import string


def calc_duration(func):
    def decorated(*args, **kwargs):
        start_time = time()
        result_func = func(*args, **kwargs)
        end_time = time()
        print(f"Executing took: {time_to_finish-time_to_start}.")
        return result_func
    return decorated


@calc_duration
def long_executing_task():  # func(*args, **kwargs) ==== long_executing_task
    for index in range(3):
        print(f'Iteration {index + 1}')
        sleep(random())


def suppress_errors(errors):
    def decorator(func):
        def decorated(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except errors as e:
                print(f"error: {e}")
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


def result_between(value_min, value_max):
    def decorator(func):
        def decorated(*args, **kwargs):
            result = func(*args, **kwargs)
            if value_min <= result <= value_max:
                return result
            else:
                return ValueError
        return decorated
    return decorator


def len_more_than(s_len):
    def decorator(func):
        def decorated(*args, **kwargs):
            result_func = func(*args, **kwargs)
            if len(result_func) >= s_len:
                return result_func
            else:
                return ValueError
        return decorated
    return decorator


@result_between(0, 10)
def sum_of_values(numbers):
    return sum(numbers)


@len_more_than(100)
def show_message(message: str) -> str:
    return f'Hi, you sent: {message}'


def replace_commas(func):
    def decorated(*args, **kwargs):
        result_func = func(*args, **kwargs)
        for i in list(string.punctuation):
            result_func = result_func.replace(i, ' ')
        return result_func
    return decorated


def words_title(func):
    def decorated(*args, **kwargs):
        result_func = func(*args, **kwargs)
        whitespace_positions = []
        n = 0
        for i in result_func:
            if i == ' ':
                whitespace_positions.append(n)
            n += 1
        list_result = list(result_func)
        for i in range(whitespace_positions.__len__()):
            if i == 0:
                list_result[whitespace_positions[0] + 1] = str(list_result[whitespace_positions[0] + 1]).upper()
            elif i == whitespace_positions.__len__() - 1:
                list_result[whitespace_positions[whitespace_positions.__len__() - 1] - 1] = \
                    str(list_result[whitespace_positions[whitespace_positions.__len__() - 1] - 1]).upper()
            else:
                list_result[whitespace_positions[i] - 1] = str(list_result[whitespace_positions[i] - 1]).upper()
                list_result[whitespace_positions[i] + 1] = str(list_result[whitespace_positions[i] + 1]).upper()
        return ''.join(list_result)
    return decorated


@words_title
@replace_commas
def process_text(text: str) -> str:
    return text.replace(':', ',')


@replace_commas
@words_title
def another_process(text: str) -> str:
    return text.replace(':', ',')


def cache_result():
    _cache_result = {}

    def decorator(func):
        def decorated(*args, **kwargs):
            if args not in _cache_result:
                _cache_result[args] = func(*args, **kwargs)
            return _cache_result[args]
        return decorated
    return decorator


@cache_result()
def some_func(last_name, first_name, age):
    return f'Hi {last_name} {first_name}, you are {age} years old'
