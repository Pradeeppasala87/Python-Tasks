class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

employees = {}

while True:
    try:
        name = input("Name (stop to end): ")
        if name == "stop":
            break

        salary = float(input("Salary: "))

        employees[name] = Employee(name, salary)

    except:
        print("Invalid salary!")

for name, emp in employees.items():
    print(name, emp.salary)


file = open("emp.txt", "w")

for name, emp in employees.items():
    file.write(name + " " + str(emp.salary) + "\n")

file.close()
