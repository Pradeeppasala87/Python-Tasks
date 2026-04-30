file = open("employees.txt", "r")

max_salary = 0
max_name = ""

for line in file:
    name, salary = line.split()
    salary = int(salary)
    
    print(name, salary)
    
    if salary > max_salary:
        max_salary = salary
        max_name = name

file.close()

print("Highest Salary:", max_name, max_salary)

# Add new employee
name = input("Enter name: ")
salary = input("Enter salary: ")

file = open("employees.txt", "a")
file.write(name + " " + salary + "\n")
file.close()
