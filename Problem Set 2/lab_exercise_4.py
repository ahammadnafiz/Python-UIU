'''
Write a program that will take the number N as user input. Next, the user will enter
those N numbers and compute their average.
'''

test_cases = int(input())  # Prompt the user to input the number of test cases and convert it to an integer

n = list(map(float, input().split()))  # Prompt the user to input a space-separated list of numbers and convert them to a list of floats

s = 0  # Initialize a variable s with the value 0 to store the sum of the numbers
for i in n:  # Iterate through each number in the list
    s += i  # Add the current number to the sum

print(f"Average: {s / test_cases}")  # Calculate the average by dividing the sum by the number of test cases and print it with a formatted string

