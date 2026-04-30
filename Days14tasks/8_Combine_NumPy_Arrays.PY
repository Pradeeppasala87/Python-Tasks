import numpy as np
import pandas as pd

names = np.array(["A", "B", "C"])
marks = np.array([80, 90, 70])

df = pd.DataFrame({"Name": names, "Marks": marks})

filtered = df[df["Marks"] > 75]

print(df)
print(filtered)
