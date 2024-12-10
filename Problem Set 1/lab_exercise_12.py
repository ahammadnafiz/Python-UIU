# lab_exercise_12.py
'''Robin Hood steals money from the rich and gives it to the poor, but conditionally.
Before deciding to steal, he sees the population of his town at a particular hour. If the
number of rich people in the town is more than the number of poor people, he does
not steal. If he sees that the number of poor people is more than the number of rich
people, he will only steal if both:
● The number of poor people is a multiple of 4.
● The number of rich people is a multiple of 3.
Write a program for Robin Hood where he will input the number of poor people and
the number of rich people. The program will tell whether or not Robin Hood should
steal at that time of the day. The program will output either “Do not steal” or “Steal”'''

rich_people = int(input('Number of rich people: '))
poor_people = int(input('Number of poor people: '))

if rich_people > poor_people:
    print('Do not steal')
else:
    if poor_people % 4 == 0 and rich_people % 3 == 0:
        print('Steal')
    else:
        print('Do not steal')
    print()
print()
