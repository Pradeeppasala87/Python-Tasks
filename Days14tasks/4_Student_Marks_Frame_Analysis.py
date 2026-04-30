import pandas as pd
data = pd.DataFrame({
    "Name": ["A", "B", "C"],
    "Math": [80, 70, 60],
    "Science": [90, 60, 70]
})

data["Total"] = data["Math"] + data["Science"]


print(data.loc[data["Total"].idxmax()])
