import numpy as sp

code = sp.array([2, 4, 1, 4, 3, 4, 5])
value = sp.where(code == 4)[0]
       
print(value)     
