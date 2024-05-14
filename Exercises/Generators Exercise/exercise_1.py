'''
 Write a Python program that creates a generator function that yields cubes of numbers from 1 to n. Accept n from the user.
'''

def cube_generator(n):
    for i in range(1, n + 1):
        yield i ** 3

n = int(input('Enter Number: '))

cubes = cube_generator(n)

for i in cubes:
    print(i)
