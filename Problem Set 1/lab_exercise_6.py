# lab_exercise_6.py

'''Celsius to
Fahrenheit conversion'''


while True:
    choice = int(input("Enter the choice of conversion: "))


    if choice == 1:
        Celsius = int(input("Enter the temperature in Celsius: "))
        Fahrenheit = int((Celsius * 1.8) + 32)
        print(f"The converted temperature is: {Fahrenheit} F")
        break
    elif choice == 2:
        Fahrenheit = int(input('Enter the temperature in Fahrenheit: '))
        Celsius = int(((Fahrenheit - 32) * 5) / 9)
        print(f"The converted temperature is: {Celsius} C")
        break
    else:
        print('Please enter 1 or 2 for conversion')

print()
