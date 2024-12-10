# lab_exercise_2.py

'''Write a program to take a number as input from the user and check if the number is
odd or even. Print the label: "The number is odd/even".'''

# Method 1

number = int(input('Enter a number: '))
if number % 2 == 0:
    print('The number is even')
else:
    print('The number is odd')

# Method 2

num = int(input('Enter a number: '))
if num & 1 == 0:
    print('The number is even')
else:
    print('The number is odd')
    