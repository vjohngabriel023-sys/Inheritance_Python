print(" ~~Hybrid Inheritance~~")

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Heyow, I'm {self.name}."


class Employee(Person):
    def role(self):
        return f"{self.name} is an employee"


class Project:
    def __init__(self, project_name):
        self.project_name = project_name


class TeamLead(Employee, Project):
    def __init__(self, name, project_name, team_size):
       
        Person.__init__(self, name)
        Project.__init__(self, project_name)
        self.team_size = team_size

    def details(self):
        return f"{self.role()}, and leads project '{self.project_name}' with {self.team_size} members."

lead = TeamLead("Gab", "Web App Launch", 3)
print(lead.greet())
print(lead.role())
print(lead.details())
print("-" * 30)
