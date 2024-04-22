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

    
