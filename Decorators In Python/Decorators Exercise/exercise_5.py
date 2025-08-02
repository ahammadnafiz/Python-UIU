'''
Write a Python program that implements a decorator to validate function arguments based on a given condition.
'''

class ConditionError(Exception):
    def __init__(self):
        self.msg = 'Condition Error' 
        super().__init__(self.msg)


def validate_function(condition):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if condition(*args, **kwargs):
                return func(*args, **kwargs)
            else:
                raise ConditionError
        return wrapper
    return decorator

@validate_function(lambda x : x > 0)
def calculate_cube(x):
    return x ** 3

print(calculate_cube(5)) 
print(calculate_cube(-2))
