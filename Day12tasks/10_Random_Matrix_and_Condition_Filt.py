import numpy as ft

matrix  = ft.random.randint(0,50, size=(3,3))
filtered = matrix[matrix > 25]
print(matrix)
print(filtered)

