'''
Write a program to take a number N as user input and generate a binary number in one
line. The length of the number is N. (print 0s and 1s up to N).
'''


for i in range(1, int(input()) + 1):  # Iterate through numbers from 1 to n (inclusive)
    if i % 2 == 0:  # Check if the number is even
        print(0, end='')  # Print 0 if the number is even
    else:
        print(1, end='')  # Print 1 if the number is odd