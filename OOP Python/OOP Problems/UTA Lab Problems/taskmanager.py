class Task:
    def __init__(self, title, description, status="To Do", assigned_to=None):
        self.title = title
        self.description = description
        self.status = status
        self.assigned_to = assigned_to

    def update_status(self, new_status):
        self.status = new_status
        print(f"Task '{self.title}' status updated to: {self.status}")

    def assign(self, user):
        self.assigned_to = user
        print(f"Task '{self.title}' assigned to: {user.name}")

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.tasks = []

    def assign_task(self, task):
        self.tasks.append(task)
        task.assign(self)

    def complete_task(self, task):
        if task in self.tasks:
            task.update_status("Done")
            print(f"{self.name} completed task: {task.title}")
        else:
            print(f"Task '{task.title}' not assigned to {self.name}")

class Project:
    def __init__(self, name):
        self.name = name
        self.tasks = []
        self.team = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task.title}' added to project '{self.name}'")

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Task '{task.title}' removed from project '{self.name}'")
        else:
            print(f"Task '{task.title}' not found in project '{self.name}'")

    def add_team_member(self, user):
        self.team.append(user)
        print(f"{user.name} added to project '{self.name}'")

    def remove_team_member(self, user):
        if user in self.team:
            self.team.remove(user)
            print(f"{user.name} removed from project '{self.name}'")
        else:
            print(f"{user.name} not found in project '{self.name}'")

class TaskManager:
    def __init__(self):
        self.projects = []

    def create_project(self, name):
        project = Project(name)
        self.projects.append(project)
        print(f"Project '{name}' created")
        return project

    def assign_task(self, task, user):
        user.assign_task(task)

    def get_user_tasks(self, user):
        return user.tasks

# Demonstration
if __name__ == "__main__":
    # Create a TaskManager
    task_manager = TaskManager()

    # Create a project
    project = task_manager.create_project("Web Development")

    # Create users
    alice = User("Alice", "alice@example.com")
    bob = User("Bob", "bob@example.com")

    # Add users to the project
    project.add_team_member(alice)
    project.add_team_member(bob)

    # Create tasks
    task1 = Task("Design homepage", "Create a responsive design for the homepage")
    task2 = Task("Implement login", "Develop user authentication system")

    # Add tasks to the project
    project.add_task(task1)
    project.add_task(task2)

    # Assign tasks to users
    task_manager.assign_task(task1, alice)
    task_manager.assign_task(task2, bob)

    # Update task status
    task1.update_status("In Progress")
    bob.complete_task(task2)

    # Show tasks for each user
    print("\nAlice's tasks:")
    for task in task_manager.get_user_tasks(alice):
        print(f"- {task.title} ({task.status})")

    print("\nBob's tasks:")
    for task in task_manager.get_user_tasks(bob):
        print(f"- {task.title} ({task.status})")

    # Show tasks in the project
    print(f"\nTasks in project '{project.name}':")
    for task in project.tasks:
        print(f"- {task.title} ({task.status}), Assigned to: {task.assigned_to.name}")

    # Demonstrate shared tasks between User and Project
    print("\nDemonstrating shared tasks:")
    print(f"Task '{task1.title}' in Alice's tasks: {task1 in alice.tasks}")
    print(f"Task '{task1.title}' in project tasks: {task1 in project.tasks}")