import numpy as py

data = py.array([12, 7, 25, 3, 18, 10])
data.sort()
split = py.split(data,2)
math = py.sum(data)

print('the sort is ascending order:',data)
print('the split is equal two:',split)
print('adding the list to each number:',math)
                  
