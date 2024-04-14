student_data = {
'Emma': {'name': 'Emma', 'major':
'Computer Science', 'cgpa': 3.8,
'completed_credits': 90},
'Daniel': {'name': 'Daniel', 'major':
'Electrical Engineering', 'cgpa': 3.5,
'completed_credits': 75},
'Sophia': {'name': 'Sophia', 'major':
'Mechanical Engineering', 'cgpa': 3.2,
'completed_credits': 60}
}

new_dict = {}
for key, value in student_data.items():
    temp_dict = {}
    for k, v in value.items():
        if k == 'cgpa':
            temp_dict[k] = v
        elif k == 'completed_credits':
            temp_dict[k] = v
    new_dict[key] = temp_dict

print(new_dict)