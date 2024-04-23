# Decorators
'''
Decorators are functions that 'decorates' other functions
We essentially wrap a function around other function
'''

# Visual
'''
def func():
        ---> func()

decorator func
def func():         
            ---> func(func())
                        |
                        ---> original func
'''
# That way we can give a function exta functionality without changing it

'''
For example, we can create a decorator for a function that makes the function execute twice when called
'''
# Decorators in classes allow you to run code when an attribute is accessed or changed

def func():
    print('Function')

def wrapper(func):
    print('Hello')
    func()
    print('GoodBye')

wrapper(func)   # passing func object to wrapper function

def function_generator():
    def new_function():
        print('New Function')
    return new_function

new_function = function_generator()
new_function()

# Example - 1
def decorator(func):
    def wrapper(*args, **kwargs):
        print('Decoration begins')
        func(*args, **kwargs)
        print('Decoration ends')
    return wrapper

@decorator
def func():
    print('Function')

#func = decorator(func)
func()

# Example - 2
import time

def duration_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Duration: {end-start}")
    return wrapper

@decorator
@duration_decorator
def func(n):
    L = [i for i in range(n)]

func(100000)

# Example - 3
def double_decorator(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper

@double_decorator
@decorator
@duration_decorator
def func(n):
    L = [i for i in range(n)]

func(100000)

# Example - 4
def repetition_decorator(repetitions):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for r in range(repetitions):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repetition_decorator(4)
def func():
    print('Hello')
func()

# Decorator inside of class
'''
@property allows you to turn methods into attributes
this comes form the property function
'''

class Generic:
    def __init__(self):
        self._x = 10
    def getter(self):
        return self._x
    def setter(self, value):
        self._x = value
    def deleter(self):
        del self._x
    x = property(getter, setter, deleter)

generic = Generic()
generic.x = 5
print(generic.x)

# Same as

class Generic:
    def __init__(self):
        self._x = 10
    
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x

generic = Generic()
generic.x = 5
print(generic.x)

