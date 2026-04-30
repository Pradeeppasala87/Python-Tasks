"""============================================================
Project Title:House Sales (kc_house_data.csv)
Analyze House Sales dataset using NumPy, Pandas, Matplotlib
============================================================

============================================================
                 Import Required Libraries
============================================================"""
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

#====================================================================================================
#               Scenario 1: Data Loading & Basic Cleaning
#====================================================================================================
"""1. Load the dataset using Pandas. 
2. Display: 
○ First 5 rows 
○ Column names 
3. Check for missing values in: 
○ bedrooms 
○ bathrooms 
○ sqft_living 
○ price 
4. Fill missing values: 
○ bedrooms → use mode 
○ bathrooms → use mean 
○ sqft_living → use mean 
○ price → use mean 
5. Convert these columns to numeric if required: 
○ bedrooms 
○ bathrooms 
○ sqft_living 
○ price """

# 1. Load the dataset
df = pd.read_csv("kc_house_data.csv")

# 2. Display first 5 rows
print("First 5 rows:")
print(df.head())
print("========================================================")

# Display column names
print("\nColumn Names:")
print(df.columns)
print("========================================================")

# 3. Check for missing values
cols = ['bedrooms', 'bathrooms', 'sqft_living', 'price']
print(df[cols].isnull().sum())
print("========================================================")
print("========================================================")

# 4. Convert columns to numeric (if required)
for col in cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# 5. Fill missing values
# bedrooms → mode
df['bedrooms'].fillna(df['bedrooms'].mode()[0])

# bathrooms → mean
df['bathrooms'].fillna(df['bathrooms'].mean())

# sqft_living → mean
df['sqft_living'].fillna(df['sqft_living'].mean())

# price → mean
df['price'].fillna(df['price'].mean())

#====================================================================================================
# Scenario 2: Line Graph + Save
#====================================================================================================
 
"""1. Select: 
○ id 
○ price 
2. Take the first 10 rows only. 
3. Convert price into a NumPy array. 
4. Plot a line graph: 
○ X-axis → index (0–9) 
○ Y-axis → Price 
5. Add: 
○ Title 
○ X-label 
○ Y-label 
6. Save the graph: plt.savefig("house_prices_line.png")"""

# 2.1. Select required columns
data = df[["id", "price"]]
print("\n(S2) Selecting required columns\n", data)
print("========================================================")

# 2.2 Take first 10 rows
data = data.head(10)
print("\n(S2) Data (first 10 rows)\n", data)
print("========================================================")
print("========================================================")

# 2.3. Convert price to NumPy array
prices = data["price"].to_numpy()

# 2.4. Plot line graph
plt.figure(figsize=(10, 6))
plt.plot(range(len(prices)), prices, marker='o')

# 2.5. Add title and labels
plt.title("Line Graph Of Price Variation of First 10 Records")
plt.xlabel("Index (0–9)")
plt.ylabel("Price")

plt.grid(True)

# 6. Save the graph
plt.savefig("Line Graph Of house_prices_line.png")

# Show plot
plt.show()

#================================================================
# Scenario 3: Filtering + Bar Chart + Save
#================================================================
"""You want to analyze expensive houses. 
Tasks: 
1. Filter houses where: 
    ○ price > 1000000 
2. Count number of houses per: 
    ○ bedrooms 
3. Select top bedroom categories. 
4. Convert results to NumPy arrays. 
5. Plot a bar chart: 
    ○ X-axis → Bedrooms 
    ○ Y-axis → Count 
6. Rotate labels if needed. 
7. Save graph: plt.savefig("expensive_houses_bar.png")"""

# 1. Filter houses where price > 1,000,000
expensive_houses = df[df['price'] > 1000000]
print("(S3)Filtering houses through price > 1000000", expensive_houses)
print("========================================================")

# 2. Count number of houses per bedrooms
bedroom_counts = expensive_houses['bedrooms'].value_counts()
print("(S3)Counting Number of houses per bedrooms", bedroom_counts)
print("========================================================")
print("========================================================")

# 3. Select top bedroom categories (e.g., top 5)
top_bedrooms = bedroom_counts.head(5)

# 4. Convert results to NumPy arrays
bedrooms = top_bedrooms.index.to_numpy()
counts = top_bedrooms.values

# 5. Plot bar chart
plt.figure(figsize=(8, 5))
plt.bar(bedrooms, counts)

plt.xlabel("Bedrooms")
plt.ylabel("Count of Expensive Houses")
plt.title("Bar Graph Of Top Bedroom Categories (Price > 1,000,000)")

# 6. Rotate labels if needed
plt.xticks(rotation=45)

# 7. Save graph
plt.savefig("Bar Graph Of expensive_houses_bar.png")

# Optional: show plot
plt.show()

#====================================================================================================
# Scenario 4:  Pie Chart (Bedroom Distribution) + Save
#====================================================================================================

"""You want to see the distribution of house types. 
Tasks: 
1. Count number of houses by: 
    ○ bedrooms 
2. Select top 5 bedroom categories. 
3. Prepare: 
    ○ Labels 
    ○ Values 
4. Plot a pie chart. 
5. Add percentage labels. 
6. Save graph: plt.savefig("bedroom_distribution.png") """

# 1. Count number of houses by bedrooms
bedroom_counts = df['bedrooms'].value_counts()
print("\n(S4)counting number of houses bedrooms", bedroom_counts)
print("========================================================")

# 2. Select top 5 bedroom categories
top5 = bedroom_counts.head()
print("\n(S4)Selecting Top 5 bedroom categories", top5)
print("========================================================")
print("========================================================")

# 3. Prepare labels and values
labels = top5.index.astype(str)
values = top5.values

# 4. Plot pie chart
plt.figure(figsize=(7, 7))
explode = (0.1, 0.1, 0, 0, 0)
plt.pie(values, labels=labels, explode = explode, shadow = True, autopct='%1.1f%%', startangle=90)

# 5. Add title
plt.title("Pie Chart Of Bedroom Distribution (Top 5 Categories)")

# Make pie chart circular
plt.axis('equal')

# 6. Save graph
plt.savefig("Pie Chart Of bedroom_distribution.png")

# Show plot
plt.show()


#====================================================================================================
# Scenario 5: Advanced Analysis + Multiple Graphs 
#====================================================================================================
'''
Part 1: Feature Creation 
Create a new column: 
Price Category 
● price >= 1000000 → "Luxury" 
● 500000 – 999999 → "Mid Range" 
● < 500000 → "Affordable" 
Part 2: NumPy Usage 
1. Convert price column to a NumPy array. 
2. Calculate price differences using: 
np.diff() 
Part 3: Visualizations 
Line Graph 
Plot price trend for all houses. 
Stacked Bar Chart 
Show count of Price Category per Bedrooms. 
Histogram 
Plot distribution of: 
● price 
Part 4: Save All Graphs 
plt.savefig("price_trend.png") 
plt.savefig("price_category_stacked.png") 
plt.savefig("price_histogram.png") 
Part 5: Insights 
Answer these: 
1. Which bedroom category has the most expensive houses? 
2. Which price category is most common? 
3. What is the distribution pattern of house prices? 
○ Right-skewed? 
○ Normal? 
○ Concentrated in a lower price range? 
'''
#5.1 Creating a new column
df2=df.copy()
df2["Price Category"]=np.where(df2["price"]>=1000000,"Luxury",np.where(df2["price"]>=500000,"Mid Range","Affordable"))
#print(df2["Price Category"].head())
print(df2)
#5.2 converting Price column to numpy array
Prices=df2["price"].to_numpy()
Price_diff=np.diff(Prices)
#print("Difference:\n",Price_diff)
#5.3 Visualization
#Line graph
plt.figure(figsize=(10,6))
plt.plot(df2.index,df2["price"],linewidth=0.8)
plt.title("Price trends for all houses")
plt.xlabel("Index")
plt.ylabel("Price")
plt.grid(True)
plt.tight_layout()
plt.savefig("price_trend.png")
plt.show()
#Stacked Bar chart
stacked=df2.groupby(["bedrooms","Price Category"]).size().unstack(fill_value=0)
stacked.plot(kind="bar",stacked=True,color=["steelblue","orange","green"],figsize=(10,6))
plt.title("Price Category per Bedroom")
plt.xlabel("Bedrooms")
plt.ylabel("Count of price categories")
plt.xticks(rotation=45)
plt.legend(title="Price Category")
plt.tight_layout()
plt.savefig("price_category_stacked.png")
plt.show()
#Histogram
plt.figure(figsize=(10,6))
plt.hist(df2["price"],bins=10,edgecolor="black",color="steelblue")
plt.title("Price Distribution")
plt.xlabel("Price")
plt.ylabel("frequency")
plt.tight_layout()
plt.savefig("price_histogram.png")
plt.show()
#part 5 Insights
#5.1 Which bedroom category has the most expensive houses?
avg_category=df2.groupby("bedrooms")["price"].mean()
expensive_category=avg_category.idxmax()
print(f"Houses with {expensive_category} bedrooms are the most expensive")
#5.2 Most common category
common_category=df2["Price Category"].value_counts().idxmax()
print(f"Most common price category:{common_category}")

#5.3 distribution pattern of house prices
mean_price=df2["price"].mean()
median_price=df2["price"].median()
skewness=df2["price"].skew()

print(f"Mean price:{mean_price}")
print(f"Median price:{median_price}")
print(f"Skewness:{skewness}")

if skewness>0.5:
    pattern="Right Skewed - Most houses are affordable" 
elif skewness<-0.5:
    pattern="Left Skewed - Most houses are expensive"
else:
    pattern="Normal - Prices are even"

print("Pattern:",pattern)






