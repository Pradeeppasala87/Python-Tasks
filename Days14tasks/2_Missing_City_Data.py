import pandas as pd
cities = {"Delhi": 2000000, "Mumbai": 3000000, "Chennai": 1500000}

S = pd.Series(cities, index=["Delhi", "Chennai", "Bangalore"])

print("\n2. Missing Data:")
print(S)
print("Missing values:")
print(S.isna())
