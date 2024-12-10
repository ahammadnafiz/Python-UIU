'''
Write a program that will take the number N as input. Next, print the sum of the first Nth
terms for the series:
1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, .......
'''


n = int(input())  # Prompt the user to input an integer

series = []  # Initialize an empty list to store the series of numbers

for i in range(1, n + 2):  # Iterate from 1 to (n + 1)
    if i % 2 == 0:  # Check if i is even
        series += [-i]  # If i is even, append its negation to the series list
    else:
        series += [i]  # If i is odd, append it to the series list

print(sum(series))  # Print the sum of all numbers in the series
print(series[n])  # Print the nth number in the series