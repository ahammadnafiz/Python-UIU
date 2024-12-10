from datetime import date


class Company:
    def __init__(self) -> None:
        self.all_employee = []
        self.projects = []

    def add_project(self, project):
        self.projects.append(project)

    def add_employee(self, employee):
        self.all_employee.append(
            {
                'name': employee.name,
                'employee_id': employee.employee_id,
                'contact_info': employee.contact_info,
                'position': employee.position
            }
        )

    def display_info(self):
        for employee in self.all_employee:
            print(f"Name: {employee['name']}\nPosition: {employee['position']}\nContact: {employee['contact_info']}")
        print()


class Person:
    def __init__(self, name, person_id, contact_info) -> None:
        self.name = name
        self._person_id = person_id
        self.contact_info = contact_info

    def get_details(self):
        print(f"Name: {self.name}\nContact Info: {self.contact_info}")

    def get_id(self):
        return self._person_id


class Employee(Person):
    def __init__(self, name, person_id, contact_info, employee_id, position) -> None:
        super().__init__(name, person_id, contact_info)
        self.employee_id = employee_id
        self.position = position
        self.projects_assigned = []

    def assign_project(self, project):
        for p in self.projects_assigned:
            if p.project_code == project.project_code:
                print(f'Project Already assigned to {p.project_manager.name}')
                return
        self.projects_assigned.append(project)

    def remove_project(self, project):
        for p in self.projects_assigned:
            if p.project_code == project.project_code:
                self.projects_assigned.remove(p)
                print('Project removed')
                return
        print('Project is not found in the list')

    def search_project(self, project):
        for p in self.projects_assigned:
            if p.project_code == project.project_code:
                print(f"Project Name: {p.project_name}")
                for k, v in p.attributes.items():
                    print(f"{k}: {v}")
                return
        print("Project not found")

    def complete_project(self):
        print(f"{self.name} completed the project")


class Project:
    def __init__(self, project_code, project_name, project_manager, start_date, end_date=None, **kwargs):
        self.project_code = project_code
        self.project_name = project_name
        self.project_manager = project_manager
        self.start_date = start_date
        self.end_date = end_date
        self.profits = 0
        self.attributes = kwargs

    def complete_project(self, profit):
        self.end_date = date.today()  # Set the end date to the current date when completing the project
        self.profits += profit


class Manager(Employee):
    def __init__(self, name, person_id, contact_info, employee_id, position, department) -> None:
        super().__init__(name, person_id, contact_info, employee_id, position)
        self.team_members = []
        self.department = department
        self.budget_allocated = 0

    def add_team_member(self, employee):
        for e in self.team_members:
            if e.employee_id == employee.employee_id:
                print(f"{e.name} already in the team")
                return
        self.team_members.append(employee)

    def remove_team_member(self, employee):
        for e in self.team_members:
            if e.employee_id == employee.employee_id:
                self.team_members.remove(employee)
                print(f"{e.name} removed from the team")
                return
        print("Member doesn't exist in the team")

    def search_team_member(self, employee):
        for e in self.team_members:
            if e.employee_id == employee.employee_id:
                print(f"Name: {e.name}\nPosition: {e.position}")
                return
        print("Team member not found")

    def allocate_budget(self, amount):
        self.budget_allocated += amount


class CEO(Manager):
    def __init__(self, name, person_id, contact_info, employee_id, position, department) -> None:
        super().__init__(name, person_id, contact_info, employee_id, position, department)
        self.direct_reports = []

    def add_direct_report(self, manager):
        self.direct_reports.append(manager)

    def remove_direct_report(self, manager):
        for m in self.direct_reports:
            if m.employee_id == manager.employee_id:
                self.direct_reports.remove(manager)
                print(f"{m.name} removed")
                return
        print('Manager is not in the direct reports')

    def show_report(self):
        for manager in self.direct_reports:
            print(f"Manager ID: {manager.employee_id}, Manager Name: {manager.name}, Team Size: {len(manager.team_members)}")


class FinancialSystem:
    def __init__(self, total_budget, expenses, profits) -> None:
        self.__total_budget = total_budget
        self.__expenses = expenses
        self.__profits = profits

    def get_budget(self):
        return self.__total_budget

    def get_expenses(self):
        return self.__expenses

    def get_profits(self):
        return self.__profits

    def calculate_profits(self, c):
        total_profits = sum(project.profits for project in c.projects)
        return total_profits


c = Company()


# Create Employees
employee1 = Employee("John Doe", 1, "john@example.com", 101, "Developer")
employee2 = Employee("Jane Smith", 2, "jane@example.com", 102, "Designer")

# Create Manager
manager1 = Manager("Manager One", 3, "manager@example.com", 201, "Project Manager", "Development")

# Create CEO
ceo = CEO("CEO Person", 4, "ceo@example.com", 301, "CEO", "Executive")

# Assign Employees to Manager
manager1.add_team_member(employee1)
manager1.add_team_member(employee2)

# Assign Manager to CEO
ceo.add_direct_report(manager1)

# Create Projects
project1 = Project("P001", "Project One", manager1, date(2024, 3, 1))
project2 = Project("P002", "Project Two", manager1, date(2024, 3, 1))

# Assign Projects to Employee
employee1.assign_project(project1)
employee2.assign_project(project2)

# Display Company Information
c.add_employee(employee1)
c.add_employee(employee2)
c.add_employee(manager1)
c.add_employee(ceo)
c.add_project(project1)
c.add_project(project2)

c.display_info()

# Display Manager's Team
manager1.search_team_member(employee1)

# Display CEO's Direct Reports
ceo.show_report()

# Complete a Project
project1.complete_project(5000)

# Calculate Profits
financial_system = FinancialSystem(100000, 20000, 0)
total_profits = financial_system.calculate_profits(c)
print(f"Total Profits: ${total_profits}")
