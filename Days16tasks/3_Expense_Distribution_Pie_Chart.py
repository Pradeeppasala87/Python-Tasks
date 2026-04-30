import numpy as np
import matplotlib.pyplot as plt


expenses = np.array([500, 300, 200])
labels = ["Food", "Rent", "Travel"]

plt.pie(expenses, labels=labels, autopct='%1.1f%%')
plt.title("Expense Distribution")
plt.show()
