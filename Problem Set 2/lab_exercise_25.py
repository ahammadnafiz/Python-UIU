'''
Write a program that would take a matrix as input. Next, find the sum of the major (top
left to bottom right) and minor (top right to bottom left) diagonals of the matrix. If the
major diagonal sum is greater, then print “Major aligned”. If the minor diagonal sum is
greater, the print “Minor aligned”. If they are the same, then print “Balanced”.

'''

matrix = []

# Input the matrix
while True:
    row = input()
    if row == "":
        break
    elements = list(map(int, row.split()))
    matrix.append(elements)

# Another Way to take single line multidimentional matrix

matrix = [[int(col) for col in row.split()] for row in iter(input, '')]

major_sum = []
minor_sum = []

# Calculate the sum of elements along the major and minor diagonals
for row in range(len(matrix)):
    for column in range(len(matrix[0])):
        if row == column:
            major_sum.append(matrix[row][column])
        if row + column == len(matrix) - 1:
            minor_sum.append(matrix[row][column])

# Print the sum of major and minor diagonal elements
print(f"Major Sum: {sum(major_sum)}\nMinor Sum: {sum(minor_sum)}")

# Determine the alignment based on the sums
if sum(major_sum) > sum(minor_sum):
    print('Major aligned')
elif sum(major_sum) < sum(minor_sum):
    print('Minor aligned')
else:
    print('Balanced')
    
print()