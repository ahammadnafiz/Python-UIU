# LEGB --> Local, Enclosed, Global, Built-in

x = 100 # Global variable

def outer():
    global x
    x += 20  # Local variable
    print(x)

#print(x)    # We can't access Local variable from outside of the function

outer()

# Enclosed/nonlocal  variable
x = 200     # global variable
def outer():
    x = 10      # nonlocal or Enclosed variable
    def inner():
        nonlocal x
        x += 10     # local variable    
        print(x)
    inner()
outer()

# LEGB rule
'''
LEGB helps Python figure out what a word (like a variable or function name) means when it's used in your code. It stands for:

L for Local: Python first checks if the word is defined in the current part of the code you're working on.
E for Enclosing: If Python doesn't find the word locally, it looks in the functions that contain the current part of the code.
G for Global: If it's still not found, Python looks at the entire file to see if the word is defined outside of any functions.
B for Built-in: If Python can't find the word anywhere in your code, it checks if it's a built-in word that's always available.
'''
# Global scope
x = 10  # global variable

def outer_func():
    # Enclosing scope
    x = 20  # nonlocal/Enclosed variable
    
    def inner_func():
        # Local scope
        x = 30  # local variable
        print(x)
    
    inner_func()
    print(x)

outer_func()
print(x)
