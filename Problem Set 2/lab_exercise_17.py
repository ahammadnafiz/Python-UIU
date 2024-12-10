'''
Write a program to take a number N as input. Now, draw a right-angled triangle using
*, up to the height N.

'''

n = int(input())  # Prompt the user to input a number

for i in range(1, n + 1):  # Iterate over the range from 1 to n (inclusive)
    for j in range(1, i + 1):  # Iterate over the range from 1 to i (inclusive)
        print('*', end=' ')  # Print an asterisk followed by a space, without a newline character
    print()  # Print a newline character to move to the next line after printing the asterisks in the current row