import numpy as yp

data1 = yp.array([[10, 20],[30, 40]])
data2 = yp.array([[5, 15],[25, 35]])
matrix = (data1 + data2)  
total_employees = yp.sum(matrix)
print("the matrix is:",matrix)
print("total employees across all departments:",total_employees)
