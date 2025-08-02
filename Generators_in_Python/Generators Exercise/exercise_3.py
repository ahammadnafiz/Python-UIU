'''
Write a Python program that creates a generator function that generates all prime numbers between two given numbers.
'''

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def prime_generator(start, end):
    for i in range(start, end):
        if is_prime(i):
            yield i

start = int(input('Enter Start: '))
end = int(input('Enter End: '))
prime_numbers = prime_generator(start, end)

for num in prime_numbers:
    print(num)
