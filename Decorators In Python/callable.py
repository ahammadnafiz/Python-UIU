# callable():-
'''
syntax --> callable(python_object)
True: if passed object is callable
False: if passed object not callable
'''

'''
object which can be called whenever required, and having __call__()method in their class
'''

x = 1

# function are callable object
def add(a, b):
    return a + b
print(type(add))

print(callable(x))      # False
print(callable(add))    # True  add.__call__()

# let's check for class
class Add:
    def __init__(self, a, b):
        self.a = a
        self.b = b

a1 = Add(1, 2)
print(callable(a1))     # False, object are not callable, because __call__ is not defined
print(callable(Add))    # True, class are callable

class Add:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __call__(self, a, b):
        return a + b

a1 = Add(1, 2)
print(a1(1, 2))         # a1.__call__(1, 2)
print(callable(a1))     # Now a1 object will be callable  

