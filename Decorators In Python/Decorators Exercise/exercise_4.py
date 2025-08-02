'''
Write a Python program that implements a decorator to cache the result of a function.
'''

def caches(func):
    cache = {}
    def wrapper(*args, **kwargs):
        keys = (*args, *kwargs.items())
        #print(keys)
        #print(cache)
        if keys in cache:
            print("Retrieving result from cache...")
            return cache[keys]

        result = func(*args, **kwargs)
        cache[keys] = result

        return result
    return wrapper

@caches
def calculate_multiply(x, y):
    print("Calculating the product of two numbers...")
    return x * y

print(calculate_multiply(4, 5))
print(calculate_multiply(4, 5))
