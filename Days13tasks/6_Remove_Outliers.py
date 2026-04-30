import numpy as np
values = np.array([10, 12, 15, 18, 100, 14, 13])
mean,std = np.mean(values), np.std(values)
filtered = values[np.abs(values - mean) <= 2* std]
print(filtered)
