'''
You are working on a program to manage the roster of a sports team. The team's roster
is represented as a list of jersey numbers, where each jersey number corresponds to a
player. However, there seems to be an issue with duplicate jersey numbers, and you
need to identify and resolve it.
Write a Python program that takes a list of jersey numbers as input and identifies and
prints the jersey numbers that have duplicates. The printing of the jersey numbers in
the output can be in any order.
'''

jersey_number = list(map(int, input().split()))  # Prompt the user to input a space-separated list of integers and convert it to a list of integers

duplicate_number = []  # Initialize an empty list to store the duplicate numbers

for i in jersey_number:  # Iterate over each element in the jersey_number list
    if jersey_number.count(i) > 1:  # Check if the count of the current number is greater than 1
        duplicate_number.append(i)  # If the number is a duplicate, append it to the duplicate_number list


# More Consise way using list comphrension
'''
duplicate_elements = list(set([x
                      for x in my_list
                      if my_list.count(x) > 1]))
'''


# Or Another way
'''
unique_elements = []
duplicate_elements = []

for i in jersey_number:
    if i not in unique_elements:
        unique_elements.append(i)
    elif i not in duplicate_elements:
        duplicate_elements.append(i)

'''


unique_duplicate_number = []  # Initialize an empty list to store the unique duplicate numbers

for j in duplicate_number:  # Iterate over each element in the duplicate_number list
    if j not in unique_duplicate_number:  # Check if the current number is not already in the unique_duplicate_number list
        unique_duplicate_number.append(j)  # If the number is unique, append it to the unique_duplicate_number list

if unique_duplicate_number:  # Check if there are unique duplicate numbers
    print(f"Duplicate jersey numbers: {' '.join(map(str, sorted(unique_duplicate_number)))}")  # Print the unique duplicate numbers in sorted order
else:
    print('No duplicates')  # If there are no unique duplicate numbers, print 'No duplicates'

