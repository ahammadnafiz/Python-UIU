'''
Write a program that will take the number N as input. Next, print the Fibonacci series up
to the length of N.
'''

n = int(input())  # Prompt the user to input an integer

a, b = 0, 1  # Initialize the first two Fibonacci numbers

for _ in range(n):  # Iterate n times
    print(b, end=' ')  # Print the Fibonacci number followed by a space
    a, b = b, a + b  # Compute the next Fibonacci number by swapping and adding the previous two numbers

print()  # Print a new line after printing all Fibonacci numbers