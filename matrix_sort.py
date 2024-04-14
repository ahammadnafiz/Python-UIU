mat = [
    [5, 4, 7],
    [1, 3, 8],
    [2, 9, 6]
]

# Print the original matrix
print("Original Matrix:")
for row in mat:
    for num in row:
        print(num, end=' ')
    print("")

# Flatten the matrix into a 1D list
elements = [num for row in mat for num in row]

# Sort the elements in ascending order
elements.sort()

# Reshape the sorted elements back to the original matrix shape
sorted_mat = []
index = 0

for _ in range(len(mat)):
    row = []
    for _ in range(len(mat[0])):
        row.append(elements[index])
        index += 1
    sorted_mat.append(row)

# Print the sorted matrix
print("\nMatrix After Sorting:")
for row in sorted_mat:
    for num in row:
        print(num, end=' ')
    print("")