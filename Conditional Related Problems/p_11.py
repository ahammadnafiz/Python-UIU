marks = float(input())

if 90 <= marks <= 100:
    grade = "A"
elif 86 <= marks <= 89:
    grade = "A-"
elif 82 <= marks <= 85:
    grade = "B+"
elif 78 <= marks <= 81:
    grade = "B"
elif 74 <= marks <= 77:
    grade = "B-"
elif 70 <= marks <= 73:
    grade = "C+"
elif 66 <= marks <= 69:
    grade = "C"
elif 62 <= marks <= 65:
    grade = "C-"
elif 58 <= marks <= 61:
    grade = "D+"
elif 55 <= marks <= 57:
    grade = "D"
elif marks < 55:
    grade = "F"
else:
    grade = "Invalid Marks"

print(f"Letter Grade: {grade}")
