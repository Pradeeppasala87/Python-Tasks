import numpy as pt
salaries = pt.array([25000, 40000, 15000, 50000, 30000])

arr = salaries > 30000
filtered = salaries[arr]
count = pt.sum(arr)
print(filtered)
print(count)
