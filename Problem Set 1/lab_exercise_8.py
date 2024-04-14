# lab_exercise_8.py

'''Write a simple program that helps users calculate the area and
perimeter/circumference of different shapes based on their choice.'''

choice = int(input('Enter choice of shape: '))

if choice == 1:
    radius = int(input('Enter the radius: '))
    print(f"Area of the circle: {3.14 * (radius ** 2)}")

elif choice == 2:
    length = int(input('Enter the length: '))
    print(f"Area of the square: {length**2}")

elif choice == 3:
    one_side = int(input('Enter the length for one side: '))
    another_side = int(input('Enter the length for another side: '))
    print(f"Area of the retangle: {one_side * another_side}")

elif choice == 4:
    base = int(input('Enter the base: '))
    height = int(input('Enter the height: '))
    print(f"Area of the triangle: {0.5 * base * height}")

print()
