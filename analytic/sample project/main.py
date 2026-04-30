import pandas as pd
import matplotlib.pyplot as plt

# Using a raw string r'' helps avoid path errors we saw earlier
df = pd.read_csv("railway_gauges.csv")

# Clean column names just in case there are hidden spaces
df.columns = df.columns.str.strip()

# Drop 'Total' if it exists so it doesn't skew the chart scale
df = df.drop(columns=['Total'], errors='ignore')

# Increase figure size so the bars/labels have room to breathe
ax = df.plot(x='Year', kind='bar', figsize=(12, 6))

plt.xticks(rotation=45) # 45 is usually easier to read than 70
plt.xlabel('Year')   
plt.ylabel('Track Count')
plt.title('Gauges: Number of railway tracks installed per year')

plt.tight_layout() # Prevents labels from getting cut off in the PNG
plt.savefig('rail_gauges.png')  
plt.show()
