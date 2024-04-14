def increaseSalary(salary,percentage=0.2):
    return salary + salary * percentage

file_path = "Employee.txt"

write_file = []

with open(file_path, "r") as file:
    employee_data = file.readlines()
    for value in employee_data:
        record = value.strip().split(',')
        salary = float(value.strip().split(',')[3])
        
        if salary < 15000:
            increased_salary = increaseSalary(salary)
        else:
            increased_salary = increaseSalary(salary, 0.15)
            
        record[3] = str(increased_salary)
        write_file.append(record)


with open(file_path, 'w') as file:
    for line in write_file:
        file.write(f"{",".join(map(str, line))}\n")
