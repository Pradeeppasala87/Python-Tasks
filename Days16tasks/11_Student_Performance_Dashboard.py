import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

marks = np.array([45, 67, 89, 56, 72, 91, 38])
students = ["A", "B", "C", "D", "E", "F", "G"]

df = pd.DataFrame({"Student": students, "Marks": marks})


plt.plot(df["Student"], df["Marks"], marker='o')
plt.title("Marks Trend")
plt.show()

plt.bar(df["Student"], df["Marks"])
plt.title("Student vs Marks")
plt.show()

pass_fail = ["Pass" if m > 50 else "Fail" for m in marks]
pd.Series(pass_fail).value_counts().plot.pie(autopct="%1.1f%%")
plt.title("Pass vs Fail")
plt.show()

plt.hist(marks, bins=5)
plt.title("Marks Distribution")
plt.show()

plt.scatter(range(len(marks)), marks)
plt.title("Index vs Marks")
plt.show()
