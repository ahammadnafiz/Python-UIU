n = int(input())


N = input()
numbers = map(float, N.split())
    
sum_num = 0
count = 0
    
for num in numbers:
    sum_num += num
    count += 1

print(f"AVG of {n} inputs: {sum_num / count}")

# Get the value of N from the user
N = int(input("Enter the value of N: "))

# Initialize sum to 0
sum_of_numbers = 0

# Input N numbers and calculate their sum
for i in range(N):
    num = float(input(f"Enter a number{i + 1}: "))
    sum_of_numbers += num

# Calculate the average
average = sum_of_numbers / N

# Display the result
print(f"The average of {N} numbers is: {average}")
