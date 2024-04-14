'''
Write a program to take two numbers N and M. N represents the number of rows of the
matrix, and M represents the number of columns. Next, take the matrix as input and
transpose the matrix

'''

row, column = list(map(int, input().split()))  # Prompt the user to enter the dimensions of the matrix

matrix = [list(map(int, input().split())) for r in range(row)]  # Prompt the user to enter the elements of the matrix

transpose = []  # Create an empty list to store the transpose of the matrix

# Create a matrix of zeros with dimensions column x row to store the transpose
for _ in range(column):  # Iterate over the column of the original matrix
    m = []  # Create an empty list to store the elements of each column
    for _ in range(row):  # Iterate over the columns of the original matrix
        m.append(0)  # Add a zero to the current column
    transpose.append(m)  # Append the column to the transpose matrix

# Calculate the transpose of the matrix
for r in range(len(matrix)):  # Iterate over the rows of the original matrix
    for c in range(len(matrix[0])):  # Iterate over the columns of the original matrix
        transpose[c][r] = matrix[r][c]  # Assign the element at the current position in the original matrix to the transposed position in the transpose matrix

print()  # Print an empty line for spacing

# Print the transpose of the matrix
for row in transpose:  # Iterate over each row in the transpose matrix
    print(*row)  # Unpack and print the elements of the row with spaces between them
    
print()
# More concise way for any multidimentional matrix

# Read matrix from input
matrix = [list(map(int, row.split())) for row in iter(input, '')]

# Transpose the matrix

transpose = [[matrix[col][row] for col in range(len(matrix))] for row in range(len(matrix[0]))]

# Print the transpose matrix
for r in transpose:
    print(*r)
    
print()

# Another more simple way

transpose = [list(row) for row in zip(*matrix)]

for row in transpose:
    print(*row)