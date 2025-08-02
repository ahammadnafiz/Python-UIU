'''
Write a Python program to create a decorator function to measure the execution time of a function.
'''

import time
import functools

def execution_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"Function {func.__name__} take {(end - start):.4f} sec")
    return wrapper

@execution_time
def main(n):
    test = [i ** i for i in range(n)]

main(1000)
