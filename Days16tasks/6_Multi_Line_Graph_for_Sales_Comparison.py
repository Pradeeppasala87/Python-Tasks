import pandas as pd
import matplotlib.pyplot as plt


data = {
    "Month": ["Jan", "Feb", "Mar"],
    "Store_A": [100, 150, 200],
    "Store_B": [90, 140, 210]
}

df = pd.DataFrame(data)

plt.plot(df["Month"], df["Store_A"], marker='o', label="Store A")
plt.plot(df["Month"], df["Store_B"], marker='o', label="Store B")

plt.legend()
plt.title("Sales Comparison")
plt.show()
