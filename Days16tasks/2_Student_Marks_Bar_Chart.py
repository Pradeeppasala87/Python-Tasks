import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

names = ["A", "B", "C", "D"]
marks = np.array([70, 85, 60, 90])

df = pd.DataFrame({"Name": names, "Marks": marks})

plt.bar(df["Name"], df["Marks"], color='skyblue')
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks")
plt.show()
