'''
Write a Python program to implement a generator that generates random numbers within a given range.
'''

import random

def random_generator(start, end):
    while True:
        yield random.randrange(start, end)

start = int(input('Enter Start: '))
end = int(input('Enter End: '))
random_numbers = random_generator(start, end)

for _ in range(5):
    print(next(random_numbers))
