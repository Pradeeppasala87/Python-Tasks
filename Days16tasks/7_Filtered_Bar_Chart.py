import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



marks = np.array([45, 80, 60, 30, 90])
names = ["A", "B", "C", "D", "E"]

df = pd.DataFrame({"Name": names, "Marks": marks})

filtered = df[df["Marks"] > 50]

plt.bar(filtered["Name"], filtered["Marks"], color='green')
plt.title("Filtered Students (Marks > 50)")
plt.show()
