import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


sales = np.array([100, 150, 200, 180, 220, 300])
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]


df = pd.DataFrame({"Month": months, "Sales": sales})

plt.plot(df["Month"], df["Sales"], marker='o')
plt.show()

plt.bar(df["Month"], df["Sales"])
plt.show()

df.set_index("Month")["Sales"].plot.pie(autopct="%1.1f%%")
plt.show()

plt.hist(sales, bins=5)
plt.show()

plt.scatter(range(len(sales)), sales)
plt.show()
