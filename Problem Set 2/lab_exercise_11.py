'''
Write a program that takes a number and then prints the reverse of that number.
[Do this problem using the while statement]
[Note: Do not use Python's shortcuts. You must strictly use the loops.]

'''


# Method 1

n = int(input())  # Prompt the user to input an integer
reversed_number = 0  # Initialize a variable to store the reversed number

while n > 0:  # Execute the block of code as long as n is greater than 0
    last_digit = n % 10  # Extract the last digit of n by performing modulo 10
    reversed_number = (reversed_number * 10) + last_digit  # Append the last digit to the reversed number
    n //= 10  # Remove the last digit from n by performing integer division by 10

print(reversed_number)  # Print the reversed number


# Method 2

n = input()  # Prompt the user to input a string or number
reversed_number_list = []  # Initialize an empty list to store the reversed elements

for i in n:  # Iterate through each character or element in the input
    reversed_number_list.insert(0, i)  # Insert the current element at the beginning of the list

reversed_number = ''.join(map(str, reversed_number_list))  # Join the reversed elements into a string
print(reversed_number)  # Print the reversed string or number


# Method 3

n = input().replace(' ', '').strip()  # Prompt the user to input a string and remove spaces and leading/trailing whitespace

reversed_n = n[::-1]  # Reverse the string using slicing
print(reversed_n) # Print the reversed string
