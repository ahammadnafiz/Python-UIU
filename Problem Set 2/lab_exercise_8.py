'''
Write a program that takes a number N as input. Next, check if the number is a prime
number or not. Recall that a prime number is a number that can be divided by only 1
and itself.
'''

import math

n = int(input())  # Prompt the user to input an integer

is_prime = True  # Initialize a boolean variable to indicate if the number is prime

if n < 2:  # Check if the number is less than 2
    is_prime = False  # If the number is less than 2, it is not prime
else:
    for i in range(2, int(math.sqrt(n)) + 1):  # Iterate through numbers from 2 up to the square root of n
        if n % i == 0:  # Check if n is divisible by the current number i
            is_prime = False  # If n is divisible by i, it is not prime
            break  # Exit the loop since we found a divisor

if is_prime:
    print('Prime')  # If the number is prime, print 'Prime'
else:
    print('Not prime')  # If the number is not prime, print 'Not prime'