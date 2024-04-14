'''
Write a program that takes a number N as input. Next, print the factorial of that number
'''


n = int(input())  # Prompt the user to input an integer

factorial = 1  # Initialize the factorial as 1

for i in range(1, n + 1):  # Iterate from 1 to n (inclusive)
    factorial *= i  # Multiply the current factorial value by the current number

print(factorial)  # Print the factorial value