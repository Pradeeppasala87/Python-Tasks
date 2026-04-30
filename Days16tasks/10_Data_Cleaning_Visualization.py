import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = np.array([100, np.nan, 200, 150, np.nan, 300])

series = pd.Series(data)


mean_val = series.mean()
series.fillna(mean_val, inplace=True)


plt.plot(series, marker='o')
plt.title("Cleaned Data Line Plot")
plt.show()


filtered = series[series > mean_val]

plt.bar(range(len(filtered)), filtered)
plt.title("Values Greater than Average")
plt.show()
