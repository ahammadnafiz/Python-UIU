'''
 Write a program to print to take a number N as input. The program should print this
diamond pattern with numbers.

'''

n = int(input())  # Prompt the user to input a number

print()  # Print an empty line for spacing

# Print the upper half of the pyramid
for i in range(1, n + 1):  # Iterate over the range from 1 to n (inclusive)
    for j in range(i, n + 1):  # Iterate over the range from i to n (inclusive) to print leading spaces
        print(' ', end=' ')  # Print a space, without a newline character
    for j in range(i, 0, -1):  # Iterate over the range from i to 0 (exclusive) to print decreasing numbers
        print(j, end=' ')  # Print the current number followed by a space, without a newline character
    for j in range(2, i + 1):  # Iterate over the range from 2 to i (inclusive) to print increasing numbers
        print(j, end=' ')  # Print the current number followed by a space, without a newline character
    print()  # Print a newline character to move to the next line after printing the numbers in the current row

# Print the lower half of the pyramid
for i in range(n - 1, 0, -1):  # Iterate over the range from n - 1 down to 1 (inclusive)
    for j in range(i, n + 1):  # Iterate over the range from i to n (inclusive) to print leading spaces
        print(' ', end=' ')  # Print a space, without a newline character
    for j in range(i, 0, -1):  # Iterate over the range from i to 0 (exclusive) to print decreasing numbers
        print(j, end=' ')  # Print the current number followed by a space, without a newline character
    for j in range(2, i + 1):  # Iterate over the range from 2 to i (inclusive) to print increasing numbers
        print(j, end=' ')  # Print the current number followed by a space, without a newline character
    print()  # Print a newline character to move to the next line after printing the numbers in the current row

print()  # Print an empty line for spacing