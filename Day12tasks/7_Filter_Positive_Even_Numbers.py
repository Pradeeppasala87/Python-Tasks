import numpy as pt

arr = pt.array([-5, 10, 15, -2, 20, 25, 30])
flatered = arr[(arr>0) & (arr % 2 == 0)]
print(flatered)
