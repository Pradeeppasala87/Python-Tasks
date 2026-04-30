import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sales = np.array([200, 300, 250, 400, 350])
profit = np.array([50, 70, 60, 90, 80])
products = ["A", "B", "C", "D", "E"]

df = pd.DataFrame({"Product": products, "Sales": sales, "Profit": profit})

plt.plot(df["Product"], df["Sales"], marker='o')
plt.show()

plt.bar(df["Product"], df["Sales"])
plt.show()

df.set_index("Product")["Sales"].plot.pie(autopct="%1.1f%%")
plt.show()

plt.hist(profit, bins=5)
plt.show()

plt.scatter(sales, profit)
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.show()
