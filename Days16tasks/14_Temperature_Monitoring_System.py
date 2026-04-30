import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

temps = np.array([28, 30, 32, 35, 33, 31, 29])
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

df = pd.DataFrame({"Day": days, "Temp": temps})

plt.plot(df["Day"], df["Temp"], marker='o')
plt.show()

plt.bar(df["Day"], df["Temp"])
plt.show()

high_low = ["High" if t > 30 else "Low" for t in temps]
pd.Series(high_low).value_counts().plot.pie(autopct="%1.1f%%")
plt.show()

plt.hist(temps, bins=5)
plt.show()

plt.scatter(range(len(temps)), temps)
plt.show()
