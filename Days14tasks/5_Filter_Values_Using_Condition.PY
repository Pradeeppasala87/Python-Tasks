import numpy as np
import pandas as pd

arr = np.array([10, 25, 30, 15, 40])

S = pd.Series(arr)

filtered = S[S > 20]
print(filtered)
