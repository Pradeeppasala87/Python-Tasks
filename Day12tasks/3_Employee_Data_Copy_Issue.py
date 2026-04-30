import copy
employees = [[101, "A"], [102, "B"], [103, "C"]]
employees1 = employees.copy()
employees[0][1] = "z"
employees2 = copy.deepcopy(employees)
employees[1][1] = "y"

print(employees)
print('\nthe shallow copy can change the reference of nested lists:\n',employees1)
print(employees)
print('\nthe deep copy cannot the original one:\n',employees2)  
