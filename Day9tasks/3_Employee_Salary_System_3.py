class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def display(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

m = Manager("Ravi", 50000)
m.display()
