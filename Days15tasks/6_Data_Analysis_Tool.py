import numpy as np
import pandas as pd

marks = np.random.randint(20, 100, 5)

df = pd.DataFrame({"Marks": marks})

print(df)

# passing students
for m in marks:
    if m >= 50:
        print("Pass:", m)

print("Mean:", np.mean(marks))
