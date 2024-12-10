'''
Write a program that will take a list as input. Next, find out the maximum element present in that list
'''

user_list = list(map(int, input().split()))  # Prompt the user to input a space-separated list of integers and convert it to a list of integers

# Method 1: Using the max() function
print(max(user_list))  # Print the maximum value in the user_list using the max() function

# Method 2: Sorting the list
print(sorted(user_list)[-1])  # Sort the user_list in ascending order, then print the last element, which will be the maximum value


# Method 3
max_number = 0  # Initialize a variable to store the maximum number and set it to 0

for i in user_list:  # Iterate over each element in the user_list
    if i > max_number:  # Check if the current element is greater than the current maximum number
        max_number = i  # If so, update the maximum number with the current element

print(max_number)  # Print the maximum number