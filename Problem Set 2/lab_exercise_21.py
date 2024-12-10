'''
Write a program to print to take a number N as input. The program should generate an
identity matrix
'''

n = int(input())  # Prompt the user to input a number

for i in range(1, n + 1):  # Iterate over the range from 1 to n (inclusive)
    for j in range(1, n + 1):  # Iterate over the range from 1 to n (inclusive)
        if i == j:  # Check if the row number is equal to the column number
            print(1, end=' ')  # Print 1 if the row number is equal to the column number
        else:
            print(0, end=' ')  # Print 0 if the row number is not equal to the column number
    print()  # Print a newline character to move to the next line after printing the elements in the current row
    
