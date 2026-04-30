import numpy as np

ratings = np.array([2, 3, 4, 5, 1])
normalized = (ratings - ratings.min())/(ratings - ratings.max())
print(normalized)
