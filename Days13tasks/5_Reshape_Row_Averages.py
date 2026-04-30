import numpy as np

data = np.arange(1, 13)

reshape = data.reshape(3,4)
average = np.mean(reshape, axis=1)
print(reshape)
print(average)
