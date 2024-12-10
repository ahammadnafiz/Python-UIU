'''
Write a program to take a number as user input. Next, print all the numbers in
descending order up to that number (print the series up to Nth terms) in a single line
'''


n = int(input())  # Prompt the user to input a value and convert it to an integer
for i in range(n, 0, -1):  # Iterate through numbers from n to 1 in descending order
    print(i, end=' ')  # Print each number followed by a space
print()  # Print a new line after the loop is finished