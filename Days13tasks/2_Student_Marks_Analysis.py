import numpy as np
marks = np.array([
                [70, 80, 90],
                [60, 75, 85],
                [50, 65, 70],
                [90, 95, 85],
                [40, 55, 60]
                ])
total = np.sum(marks, axis=1)
average = np.mean(total)
above = np.where(total > average)[0]

print(total)
print(average)
print(above)
