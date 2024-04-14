'''
Write a program to take a number N as input. Now, draw an upside-down right-angled
triangle using *

'''

n = int(input())  # Prompt the user to input a number

for i in range(1, n + 1):  # Iterate over the range from 1 to n (inclusive)
    for j in range(i, n + 1):  # Iterate over the range from i to n (inclusive)
        print('*', end=' ')  # Print an asterisk followed by a space, without a newline character
    print()  # Print a newline character to move to the next line after printing the asterisks in the current row
    