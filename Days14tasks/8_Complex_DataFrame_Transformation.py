import pandas as pd

df = pd.DataFrame({
    "Name": ["A", "B", "C", "D"],
    "Marks": [50, 80, 30, 90]
})

df["Status"] = df["Marks"].apply(lambda x: "Pass" if x >= 50 else "Fail")

passed = df[df["Status"] == "Pass"]

print(passed)

print(passed["Marks"].mean())
