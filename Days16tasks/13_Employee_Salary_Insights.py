import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

salaries = np.array([25000, 30000, 28000, 40000, 50000, 35000])
departments = ["HR", "IT", "HR", "IT", "Sales", "Sales"]

df = pd.DataFrame({"Dept": departments, "Salary": salaries})

plt.plot(df["Salary"], marker='o')
plt.show()

df.groupby("Dept")["Salary"].mean().plot(kind='bar')
plt.show()

df["Dept"].value_counts().plot.pie(autopct="%1.1f%%")
plt.show()

plt.hist(salaries, bins=5)
plt.show()

plt.scatter(range(len(salaries)), salaries)
plt.show()
