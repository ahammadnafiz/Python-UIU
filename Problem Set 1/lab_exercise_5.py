# lab_exercise_5.py

'''Write a program to check if a shape is a triangle or not. The program will take three
numbers as inputs from the user, which are the angles of the triangle (the value
should be greater than 0 degrees and less than 180 degrees). Finally, print whether
the shape is a triangle or not with simply a "Yes" or a "No".'''


a, b, c = map(int, input().split())
if 0 < a and b and c < 180:

    if a + b + c == 180:
        print('Yes')
    else:
        print('No')

else:
    print("No")