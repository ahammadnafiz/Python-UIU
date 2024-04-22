# Example
def upper(main):
    def inner():
       name =  main()
       return name.upper()
    return inner

def split_name(upper):
    def inner():
       return  upper().split()
    return inner

@split_name
@upper
def main():
    name = input('Enter name: ')
    return name

#main = split_name(upper(main))
print(main())

# Example
# single decorator in multiple function
def decor(function):
    def inner(*args):
        for num in args[1:]:
            if num == 0:
                raise ZeroDivisionError
        return function(*args)
    return inner

@decor
def div_1(a, b):
    return a / b

@decor
def div_2(a, b, c):
    return a / b / c

#div_1 = decor(div_1)
print(div_1(1, 2))

#div_2 = decor(div_2)
print(div_2(1, 2, 3))
