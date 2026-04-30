import copy
classes = ([["Math", [30, 35]], ["Science", [25, 28]]])
data = copy.deepcopy(classes)
data[0][1][0] = 99 

print(classes)
print(data)
