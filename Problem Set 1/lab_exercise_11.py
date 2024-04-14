# lab_exercise_11.py
'''You are given three positive integers a, b, and c, where a and b are the sides of a
right-angled triangle, and c is the hypotenuse. Write a program that takes these three
integers as inputs from the user, and determines if the triangle is special or not.
For a triangle to be special, it needs to satisfy the Pythagorean theorem
If the triangle is special, print “Special Triangle”. Else print “Not special”.'''

a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))

if a**2 + b**2 == c**2:
    print('Special')
else:
    print('Not special')

print()