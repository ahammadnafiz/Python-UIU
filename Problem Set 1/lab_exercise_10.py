# lab_exercise_10.py

'''Developing a payroll system for a company.'''

name = input('Enter employee name: ')
work_hours = float(input('Enter the work hours: '))
experience = float(input('Enter years of work: '))
task = int(input('Enter tasks done: '))
given = int(input('Enter tasks given: '))

productivity = task / given

if work_hours > 20 and experience >= 2:
    
    if 0.5 <= productivity <=0.69:
        print(f"{name} is eligible for the Bronze bonus.")
    elif 0.70 <= productivity <=0.89:
        print(f"{name} is eligible for the Silver bonus.")
    elif 0.90 <= productivity <= 1.00:
        print(f"{name} is eligible for the Gold bonus.")
    else:
        print(f"{name} is eligible for the Normal bonus.")

else:
    print(f"{name} is not eligible for a bonus")