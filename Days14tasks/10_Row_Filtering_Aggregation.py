import numpy as np
import pandas as pd

arr = np.array([
    [100, 200],
    [150, 250],
    [80, 120],
    [300, 400]
])

df = pd.DataFrame(arr, columns=["Sales", "Profit"])

filtered = df[df["Sales"] > 100]

avg_profit = filtered["Profit"].mean()

print(filtered)
print("Average Profit:", avg_profit)
