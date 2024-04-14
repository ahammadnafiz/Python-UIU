company_hr_register = {
    101: {'name': 'Alice', 'age': 35, 'performance': 90, 'salary': 50000},
    102: {'name': 'Bob', 'age': 58, 'performance': 98, 'salary': 70000},
    103: {'name': 'Charlie', 'age': 45, 'performance': 85, 'salary': 60000},
    104: {'name': 'David', 'age': 60, 'performance': 75, 'salary': 55000},
    105: {'name': 'Eve', 'age': 28, 'performance': 92, 'salary': 48000},
    106: {'name': 'Frank', 'age': 50, 'performance': 55, 'salary': 52000},
    107: {'name': 'Grace', 'age': 62, 'performance': 97, 'salary': 75000},
}

new_hr = {}
total_bonus = 0

for key, value in company_hr_register.items():
    
    if value['performance'] > 60:
        if value['age'] > 55 and value['performance'] > 95:
            total_bonus += 15000
        elif value['age'] > 55:
            total_bonus += 10000
        elif value['performance'] > 95:
            total_bonus += 5000    
        new_hr[key] = {'name': value['name']}
        
        
print(f'Total Employ: {len(new_hr)}')
print(f'Total Bonus Amount: {total_bonus}')
print(f'Updated Company Register: {new_hr}')
