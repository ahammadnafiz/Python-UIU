# lab_exercise_15.py

'''Pete and his friend Billy decided to buy a watermelon. They chose the biggest and the
ripest one, in their opinion. After that the watermelon was weighed, and the scales
showed a certain number of kilos. They rushed home, dying of thirst, and decided to
divide it, however they faced a hard problem.
Pete and Billy are great fans of even numbers, that's why they want to divide the
watermelon in such a way that each of the two parts weighs even number of kilos,
at the same time it is not obligatory that the parts are equal. The boys are extremely
tired and want to start their eating as soon as possible, that's why you should help
them and find out, if they can divide the watermelon in the way they want. For sure,
each of them should get a part of positive weight.
Print YES, if the boys can divide the watermelon into two parts, each of them weighing
even number of kilos; and NO in the opposite case.'''



# Prompt the user to enter the weight of the watermelon
weight = int(input('Enter watermelon weight: '))

# List to store the possible divisions
divisions = []

# Iterate through possible divisions
for i in range(1, weight):
    part_1 = i
    part_2 = weight - i
    
    # Check if both parts are even
    if part_1 % 2 == 0 and part_2 % 2 == 0:
        divisions.append((part_1, part_2))

# Check if there are valid divisions
if divisions:
    print('YES - The watermelon can be divided into two parts, each with an even number of kilos.\nPossible Divisions:')
    for division in divisions:
        print(f'Part 1: {division[0]} kilos, Part 2: {division[1]} kilos')
else:
    print('NO - The watermelon cannot be divided into two parts, each with an even number of kilos.')
