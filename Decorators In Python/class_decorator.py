class Decorator:
    def __init__(self, func):
        self.function = func
        
    def __call__(self, a, b):
        # Original functionality
        result =  self.function(a, b)
        # decoration
        return result ** 2

@Decorator
def add(a, b):
    return a + b

# Decorator
#add = Decorator(add)
print(add(1, 2))    # add.__call__(1, 2)

# Another example

class Decor:
    def __init__(self, func):
        self.function = func

    def __call__(self, *args):
        try:
            if any([isinstance(i, str) for i in args]):
                 raise TabError("Can't pass string as arguments")
            else:
                 return self.function(*args)
        except Exception as e:
            print(e)

@Decor
def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

#add = Decor(add)
print(add(1, 2, 3))

