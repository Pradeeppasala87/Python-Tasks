import numpy as np
sales = np.array([12000, 18000, 9000, 22000, 15000, 30000])
average = np.mean(sales)
filtered = sales[sales > average]
print(filtered)
