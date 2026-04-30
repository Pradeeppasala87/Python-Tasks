# ==============================================================================
#  Project Title: Car Data Analysis 
#  Analysing the Car data dataset using Numpy, Pandas and matplotlib
# ==============================================================================

#==============================================================================
#                  Importing the required libraries
#==============================================================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

'''
==================================================================================
                Scenario 1: Data Loading & Basic Cleaning
================================================================================== 
Understand the dataset structure and prepare it for analysis. 
Tasks: 
● Load the dataset using Pandas. 
● Display: 
○ First 5 rows 
○ Last 5 rows 
○ Column names 
○ Shape of dataset 
● Check data types of all columns. 
● Check for missing values in:
○ Selling_Price 
○ Present_Price 
○ Kms_Driven 
○ Fuel_Type 
● Fill missing values: 
○ Selling_Price → mean 
○ Present_Price → mean 
○ Kms_Driven → mean 
○ Fuel_Type → mode 
● Convert numeric columns to proper numeric type if required: 
○ Selling_Price 
○ Present_Price 
○ Kms_Driven 
○ Year 
● Convert Selling_Price and Kms_Driven into NumPy arrays. 
● Use NumPy to calculate: 
○ minimum selling price 
○ maximum selling price 
○ average selling price 
'''
#Load the dataset using Pandas
df=pd.read_csv("cardata.csv")
#Display: First 5 rows
print(f"Displaying First 5 rows:\n{df.head()}")
print("---------------------------------------------------------------------------------")
print(f"Displaying last 5 rows:\n{df.tail()}") #Last 5 rows
print("---------------------------------------------------------------------------------")
print(f"Column names:\n{df.columns}") #Column names
print()
print(f"Shapes of Dataset:{df.shape}\n") #Shape of dataset
print("---------------------------------------------------------------------------------")
# Checking data types of all columns.
print(df.dtypes) 
print("---------------------------------------------------------------------------------")
#Check for missing values in: Selling_Price, Present_Price, Kms_Driven, Fuel_Type
print("Missing values:")
print(df[["Selling_Price","Present_Price","Kms_Driven","Fuel_Type"]].isnull().sum())

# Fill missing values:
# Selling_Price → mean 
df["Selling_Price"]=df["Selling_Price"].fillna(df["Selling_Price"].mean())
# Present_Price → mean
df["Present_Price"]=df["Present_Price"].fillna(df["Present_Price"].mean())
# Kms_Driven → mean
df["Kms_Driven"]=df["Kms_Driven"].fillna(df["Kms_Driven"].mean())
# Fuel_Type → mode
df["Fuel_Type"]=df["Fuel_Type"].fillna(df["Fuel_Type"].mode()[0])
print("---------------------------------------------------------------------------------")

#Converting numeric columns to proper numeric type: Selling_Price, Present_Price, Kms_Driven, Year 
numeric=["Selling_Price","Present_Price","Kms_Driven","Year"]
df[numeric]=df[numeric].apply(pd.to_numeric,errors='coerce')
print(df.dtypes)

#Convert Selling_Price and Kms_Driven into NumPy arrays.
S_price=df["Selling_Price"].to_numpy()
KMs=df["Kms_Driven"].to_numpy()
print("---------------------------------------------------------------------------------")
# minimum selling price 
min_S_price=S_price.min()
print(f"Minimun Selling Price: {min_S_price}")
# maximum selling price 
max_S_price=S_price.max()
print(f"Maximum Selling Price: {max_S_price}")
# average selling price
avg_S_price=S_price.mean()
print(f"Average Selling Price: {avg_S_price:.2f}")


'''
==================================================================================
                Scenario 2: Data Loading & Basic Cleaning
==================================================================================


Tasks: 
● Select: 
  ○ Car_Name 
  ○ Selling_Price 
● Take the first 10 rows only using Pandas. 
● Convert Selling_Price into a NumPy array. 
● Plot a line graph using Matplotlib: 
  ○ X-axis → row index (0–9) 
  ○ Y-axis → Selling Price 
● Add: 
  ○ title 
  ○ x-axis label 
  ○ y-axis label 
  ○ markers 
● Save the graph with a suitable filename.
'''

import matplotlib.pyplot as plt

# Select required columns and first 10 rows
select_df = df[['Car_Name', 'Selling_Price']].head(10)

# Convert to NumPy array
selling_price = select_df['Selling_Price'].to_numpy()

# Plot
plt.figure(figsize=(8, 5))
plt.plot(range(len(selling_price)), selling_price, marker='o')

# Labels and title
plt.title("Selling Price Trend (First 10 Cars)")
plt.xlabel("Car Index (0–9)")
plt.ylabel("Selling Price")

# Save and show
plt.savefig("selling_price_trend.png")
plt.show()






