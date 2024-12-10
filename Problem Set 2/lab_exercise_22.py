'''
Write a program that would take two matrices A and B as inputs. For this question,
assume that the dimension of matrix A is 3 x 2 and the matrix B is 2 x 3. Calculate the
matrix multiplication of the two matrices in 2 x 2 dimensions. Look here on how to take
a matrix input.

'''


print('Enter matrix A')
matrix_a = [list(map(int, input().split())) for _ in range(2)]  # Prompt the user to enter elements for matrix A

print('Enter matrix B')
matrix_b = [list(map(int, input().split())) for _ in range(3)]  # Prompt the user to enter elements for matrix B

multiplication = [[0, 0], [0, 0]]  # Create an empty matrix to store the result of multiplication

# Perform matrix multiplication
for row in range(len(matrix_a)):  # Iterate over the rows of matrix A
    for col in range(len(matrix_b[0])):  # Iterate over the columns of matrix B
        for k in range(len(matrix_b)):  # Iterate over a common dimension (number of columns in matrix A or number of rows in matrix B)
            multiplication[row][col] += matrix_a[row][k] * matrix_b[k][col]  # Perform multiplication and accumulate the result

# Print the result of multiplication
for r in range(len(matrix_a)):  # Iterate over the rows of the result matrix
    for c in range(len(matrix_b[0])):  # Iterate over the columns of the result matrix
        print(multiplication[r][c], end=' ')  # Print each element of the result matrix followed by a space
    print()  # Print a newline character to move to the next row