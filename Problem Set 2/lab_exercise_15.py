'''
You are developing a salary calculation program for XYZ FinTech LLC. The company
pays its employees based on the number of hours worked and an hourly wage.
However, there are certain rules for overtime pay:
● Regular hours (up to 40 hours): Paid at the regular hourly wage.
● Overtime hours (more than 40 hours): Paid at 1.5 times each hour more than
the regular hourly wage.
The program should then print the total salary for each employee.

'''

salaries = []  # Initialize an empty list to store the calculated salaries

hours_worked = list(map(int, input('Hours Worked: ').split()))  # Prompt the user to input the hours worked for each employee and convert it to a list of integers
hourly_wage = list(map(int, input('Hourly Wage: ').split()))  # Prompt the user to input the hourly wage for each employee and convert it to a list of integers

for index, hours in enumerate(hours_worked):  # Iterate over each element and index of the hours_worked list
    wage = hourly_wage[index]  # Get the corresponding hourly wage for the current employee
    
    if hours <= 40:  # Check if the hours worked is less than or equal to 40
        salaries.append(hours * wage)  # If so, calculate the salary by multiplying the hours worked with the hourly wage and append it to the salaries list
    
    else:  # If the hours worked is greater than 40
        regular_hours = 40  # Assign 40 hours as regular hours
        overtime = hours - regular_hours  # Calculate the overtime hours
        regular_salary = regular_hours * wage  # Calculate the salary for regular hours
        overtime_salary = (wage * 1.5) * overtime  # Calculate the salary for overtime hours considering 1.5 times the hourly wage
        bonus = regular_salary + overtime_salary  # Calculate the total salary including the bonus for overtime
        salaries.append(bonus)  # Append the total salary to the salaries list

for position, salary in enumerate(salaries, start=1):  # Iterate over each calculated salary and its index, starting from 1
    print(f"Employee {position}: {int(salary)} BDT")  # Print the employee position and the corresponding salary in BDT
    

  
h_worked = list(map(int,input("Hours Worked: ").split()))
h_wage = list(map(int,input("Hourly Wage: ").split()))

for i in range (len(h_worked)):
    r_h = min(h_worked[i],40)
    o_h = max(h_worked[i] - 40, 0)
    total_salary = (r_h * h_wage[i])+(o_h * 1.5 * h_wage[i])
    print(f"Employe {i+1}: {total_salary} BDT")