'''
Write a Python program to implement a generator that generates the Collatz sequence for a given number.
'''

'''
The Collatz sequence, also known as the Collatz conjecture or 3n+1 problem, is a sequence of numbers defined by the following rules:

Start with any positive integer n.
If n is even, divide it by 2 to get n/2.
If n is odd, multiply it by 3 and add 1 to get 3n+1.
Repeat the process, using the resulting number, until you reach the number 1.
'''

def collatz_generator(n):
    while n != 1:
        yield n
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
    yield 1

n = int(input('Enter a Number: '))

collatz = collatz_generator(n)

for i in collatz:
    print(i)
