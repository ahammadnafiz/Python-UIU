def decorator(func):
    def wrapper(*args, **kwargs):
        print('Hi')
        func(*args, **kwargs)
    return wrapper

@decorator
def hello(name):
    print(name)

hello('Ahammad Nafiz')