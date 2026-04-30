import pandas as pd
df = pd.DataFrame({
    "Price": [100, 200, 300]
})

df["Discount"] = df["Price"] * 0.1
df["Final Price"] = df["Price"] - df["Discount"]


print(df)
