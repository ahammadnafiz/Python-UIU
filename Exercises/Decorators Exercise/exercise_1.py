'''
Write a Python program to create a decorator that logs the arguments and return value of a function
'''

import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_value = ','.join(str(arg) for arg in args)
        kwargs_value = ','.join(f"{k} = {v}" for k, v in kwargs.items())
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} have args value: {args_value} and kwargs value: {kwargs_value}")
        return result
    return wrapper

@log
def multiply_numbers(x, y):
    return x * y

print(multiply_numbers(10, 20))
