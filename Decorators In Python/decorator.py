# What is decoration?
'''
* adding thing to something to make more attractive/presentable
'''
# What is decorator in python?
'''
* function which takes other functions as input, add additional functionalities and returns it

function --> decorator --> modified function
it is a callable python object which modifies other function/class
'''

# Example
def decorator(function):
    def inner():
        function()      # Existing functionalities, which is welcome
        # Add new functionalities
        print('Ahammad Nafiz')
    return inner

@decorator      # with decorator syntax
def welcome():
    print('Hello')

#welcome = decorator(welcome)   # decorator function
welcome()

# Example 
def wrapper(function):
    def inner():
        result = function()     # Existing functionalities
        # add new functionalities here
        num_3 = int(input('Number 3: '))
        print(result + num_3)
    return inner

@wrapper
def addition():
    num_1 = int(input('Number 1: '))
    num_2 = int(input('Number 2: '))
    return num_1 + num_2

#addition = wrapper(addition)
addition()

