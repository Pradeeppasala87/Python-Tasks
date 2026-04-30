import numpy as np

temps = np.array([28, 32, 35, 31, 29, 40, 38])

days = temps[temps > 30]
indices = np.where(temps > 30)[0]
print(days)
print(indices)
