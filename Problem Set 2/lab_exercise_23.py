'''
Write a program to take two numbers N and M. N represents the number of rows of the
matrix, and M represents the number of columns. Next, take the matrix as input and
find the maximum number present in each row of the matrix.
'''

row, column = list(map(int, input().split()))  # Prompt the user to enter the dimensions of the matrix

matrix = [list(map(int, input().split())) for r in range(row)]  # Prompt the user to enter the elements of the matrix

max_element = []  # Create an empty list to store the maximum element of each row

# Find the maximum element in each row
for r in range(len(matrix)):  # Iterate over the rows of the matrix
    max_element.append(max(matrix[r]))  # Find the maximum element in the current row and append it to the list

# Print the maximum element in each row
for m in max_element:  # Iterate over the elements in the list
    print(m)  # Print each maximum element