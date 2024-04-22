
def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f"{k} = {v}" for k, v in kwargs.items())
        print(f"Calling: {func.__name__} with args: {args_value} and kwargs_value: {kwargs_value}")
        return func(*args, **kwargs)
    return wrapper

@debug
def greet(name, greeting='Hello'):
    return (f"{greeting}, {name}")
    

greet('Nafiz', greeting='How are you?')


