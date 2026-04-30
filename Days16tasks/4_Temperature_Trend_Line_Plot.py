import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



temps = np.array([28, 30, 32, 31, 29])

series = pd.Series(temps)

plt.plot(series, marker='o')
plt.title("Temperature Trend")
plt.grid(True)
plt.show()
