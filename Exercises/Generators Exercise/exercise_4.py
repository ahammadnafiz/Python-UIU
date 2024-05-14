'''
Write a Python program to implement a generator function that generates the Fibonacci sequence
'''

def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

n = int(input('Enter num of Fibonacci: '))
fibonacci_number = fibonacci_generator(n)

for num in fibonacci_number:
    print(num)
