# Definition of Names in Python
"""
In Python, names serve as identifiers referencing various objects such as variables, functions, classes, modules, or other entities within the codebase. They function as labels facilitating the referencing and manipulation of data or code elements, thereby enhancing the readability and manageability of programs.
"""

# Assigning a Name to a Variable
x = 10

# Assigning a Name to a Function
def greet(name):
   print("Hello, " + name + "!")

# Demonstrating Identity
print(id(x))  # Identity of x
print(id(10))  # Identity of integer 10

# Definition of Namespaces in Python
"""
Namespaces in Python constitute a systematic framework for organizing and governing identifiers such as variable names, function names, class names, etc. They play a pivotal role in mitigating naming conflicts and furnishing a structured means of accessing distinct elements within the codebase.
"""

# Types of Namespaces
"""
1. Built-in Namespace
2. Module-Level/Global Namespace
3. Local Namespace
4. Enclosed Namespace
"""

# Built-in Namespace
"""
The built-in namespace encompasses all predefined functions, exceptions, and constants furnished by Python. These entities can be directly utilized without necessitating any import statements.
"""

# Examples of Built-in Namespace
print(len("Hello"))  # Demonstrating the usage of the built-in function 'len'
print(ValueError)   # Demonstrating the usage of the built-in exception 'ValueError'
print(True)          # Demonstrating the usage of the built-in constant 'True'

# Global Namespace
"""
The global namespace in Python pertains to the outermost scope of a program, housing all built-in objects, functions, and variables pre-defined in Python. It also encompasses any variables or functions defined at the top level of a script or module. Objects within the global namespace are accessible throughout the entirety of the program.
"""

# Global Variable
x = 10

def my_func():
   print(x)  # Accessing the global variable x

my_func()  # Output: 10
print(x)   # Output: 10

# Local Namespace
"""
A local namespace in Python denotes the scope confined within a function or a class. It encompasses the names of variables and objects specifically defined within the confines of that particular function or class. These names are exclusively accessible from within the local scope and remain concealed from external visibility.
"""

a = 10

def func_1():
   a = 20
   print(dir())  # Printing the directory of the local namespace, displaying only 'a'

def func_2():
   a = 30

print(dir())  # Printing the directory of the global namespace/module level, encompassing built-in modules, variable a, and functions func_1, func_2
func_1()

# Enclosed Namespace
"""
In Python, the enclosed namespace denotes the scope situated between the local and global namespaces. It comes into existence when a nested function is defined within another function. The nested function possesses access to variables from the enclosing function's scope, alongside its own local namespace and the global namespace.
"""

# Global Variable
x = 'global'

def outer_func():
   # Enclosed Variable
   y = 'enclosed'

   def inner_func():
       # Local Variable
       z = 'local'
       print(x)  # Accessing the global variable
       print(y)  # Accessing the enclosed variable
       print(z)  # Accessing the local variable

   inner_func()

outer_func()
"""
Upon invocation of inner_func(), it can access and print values from x (from the global namespace), y (from the enclosed namespace), and z (from its local namespace).
"""

