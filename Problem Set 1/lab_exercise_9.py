# lab_exercise_9.py

'''Developing a grade-checking system for UIU.'''

grade = float(input())
if 90 <= grade <=100 or grade == 4.00:
    print("Grade A, Outstanding")
elif 86 <= grade <= 89 or grade == 3.67:
    print('Grade A-, Execellent')
elif 82 <= grade <= 85 or grade == 3.33:
    print('Grade B+, Very Good')
elif 78 <= grade <= 81 or grade == 3.00:
    print('Grade B, Good')
elif 74 <= grade <= 77 or grade == 2.67:
    print('Grade B-, Above Average')
elif 70 <= grade <= 73 or grade == 2.33:
    print('Grade C+, Average')
elif 66 <= grade <= 69 or grade == 2.00:
    print('Grade C, Below Average')
elif 62 <= grade <= 65 or grade == 1.67:
    print('Grade C-, Poor')
elif 58 <= grade <= 61 or grade == 1.33:
    print('Grade D+, Very Poor')
elif 55 <= grade <= 57 or grade == 1.00:
    print('Grade D, Pass')
elif grade < 55 or grade == 0.00:
    print('Grade F, Fail')
else:
    print('Course Incomplete, Withdraw or Repat/Retake')