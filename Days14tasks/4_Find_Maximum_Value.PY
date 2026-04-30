import numpy as np
import pandas as pd

arr = np.array([12, 45, 22, 67, 34])

S = pd.Series(arr)
print(S.max())
