import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

scores = np.array([40, 60, 80, 30, 90])

df = pd.DataFrame({"Scores": scores})

pass_count = (df["Scores"] > 50).sum()
fail_count = (df["Scores"] <= 50).sum()

plt.pie([pass_count, fail_count], labels=["Pass", "Fail"], autopct='%1.1f%%')
plt.title("Pass vs Fail")
plt.show()
