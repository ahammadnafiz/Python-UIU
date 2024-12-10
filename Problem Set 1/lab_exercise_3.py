# lab_exercise_3.py

'''Write a program to take in two variables x and y as inputs from the user. Assign the
values to each of them such that the value of x is greater than the value of y (x > y).
Find out their:
● Sum
● Difference
● Product
● Division
Finally, print each of them with a label: "Their <operation> is: <result>”.'''


x = int(input('Enter first number: '))
y = int(input('Enter second number: '))
print(f"Their sum is: {x + y}")
print(f"Their difference is: {x - y}")
print(f"Their product is: {x * y}")
print(f"Their division is: {x / y}")