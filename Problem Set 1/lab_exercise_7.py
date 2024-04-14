# lab_exercise_7.py

'''An application for a supermarket checkout'''

name = input('Enter the iterm name: ')
price = int(input('Enter the price of the item: '))
quantity = int(input('Enter the quantity of the item: '))

print(f"The total price of {name} purchased: {price * quantity} BDT")
