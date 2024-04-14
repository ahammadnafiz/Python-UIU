# lab_exercise_13.py
'''The english alphabet contains 5 vowels. Write a program to take in an input
capital/small letter from the user and print whether the alphabet is a vowel or not.'''


vowels = 'AEIOUaeiou'
alphabet = input('Enter a alphabet to check vowel: ')
if alphabet in vowels:
    print('Vowel')
else:
    print('Not a vowel')

print()
