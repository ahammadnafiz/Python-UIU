# Function as object

def outer():
    print('Hello')
print(outer)    # Function object
print(type(outer))

# Nested Function

def outer():
    print('Outer')
    def inner():
        print('Inner')
    inner()

#outer()

# Aliasing Function

new = outer # Aliasing outer Function
new()
outer()

# Closures in python

def outer():
    def inner():
        x = 100
        return x
    return inner()
print(outer())


def outer():
    def inner():
        x = 100
        return x
    return inner    # returning inner Function object

inner = outer()   # The outer Function return the inner Function object and we Aliasing it with inner
print(inner())

'''
Closure is a technique by which data gets attached to the code
Closure are Function object that remembers values in the enclosing scope even if they are not present in the memory
'''


