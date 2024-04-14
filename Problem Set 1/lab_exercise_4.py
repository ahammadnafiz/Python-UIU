# lab_exercise_4.py

'''Write a program that will take three numbers as input from a user, but it will print only
the first and last numbers and skip the middle number.'''


numbers = list(map(int, input().split()))
print(f"First value = {numbers[0]}, Last value = {numbers[-1]}")
