'''
 Write a Python program to create a decorator to convert the return value of a function to a specified data type.
'''

def data(data_type):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            type_convert = data_type(result)
            return type_convert
        return wrapper
    return decorator

@data(str)
def main(n):
    return n * n

print(main(10))
print(type(main(10)))
