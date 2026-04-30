# ============================================================
# 📊 Project Title: Railway Gauge Data Analysis
# Analyze railway gauge dataset using NumPy, Pandas, Matplotlib
# ============================================================


# ============================================================
# 📦 1. Import Required Libraries
# ============================================================
# 👉 Import numpy
# 👉 Import pandas
# 👉 Import matplotlib.pyplot
# 👉 (Optional) Import os for folder creation

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np






# ============================================================
# 📁 2. Setup Project Structure
# ============================================================
# 👉 Create a folder named "graphs"
# 👉 Ensure it does not throw error if already exists




# ============================================================
# 📂 3. Load Dataset
# ============================================================
# 👉 Load CSV file into DataFrame
# 👉 Display first 5 rows
# 👉 Display column names


df=pd.read_csv("railwaygauges1.csv")
print(df.head())
print(df.columns)
#============================================================
# 🟢 SCENARIO 1: Data Cleaning
# ============================================================
# 👉 Check missing values in dataset
# 👉 Replace missing values with 0
# 👉 Convert columns:
#     Broad Gauge
#     Metre Gauge
#     Narrow Gauge
#     Total
# 👉 Ensure all are numeric type
# 👉 Print data types after conversion




df=df.fillna(0)
print(df.dtypes)
for i in df.columns:
    if i!="Year":
        df[i]=pd.to_numeric(df[i],errors="coerce")
print(df.dtypes)

# ============================================================
# 🟢 SCENARIO 2: Line Graph (Total Tracks)
# ============================================================
# 👉 Extract Year column
# 👉 Extract Total column
# 👉 Plot line graph
# 👉 Add:
#     Title
#     X-label (Year)
#     Y-label (Total Tracks)
# 👉 Save graph inside "graphs" folder
# 👉 Display graph
# 👉 Write observation:
#     Is trend increasing or decreasing?

Year=df["Year"]
total=df["Total"]
plt.plot(Year,total,marker="o")
plt.xlabel("YEAR")
plt.ylabel("TOTAL")
plt.title("Total tracks over years")
plt.tight_layout()
plt.show()
print("Trend is increasing year by year but with some dips in later years")

# ============================================================
# 🟡 SCENARIO 3: Bar Chart (After 2000)
# ============================================================
# 👉 Filter dataset for Year > 2000
# 👉 Extract:
#     Broad Gauge
#     Metre Gauge
#     Narrow Gauge
# 👉 Create positions for bars (NumPy)
# 👉 Plot grouped bar chart
# 👉 Add:
#     Title
#     Labels
#     Legend
# 👉 Rotate X-axis labels if needed
# 👉 Save graph inside "graphs" folder
# 👉 Display graph
# 👉 Write observation:
#     Which gauge is dominant?


df["Year_in_int"]=df["Year"].str[:4].astype(int)
fil_df=df[df["Year_in_int"]>2000]

select_bmn=fil_df[["Broad Gauge","Metre Gauge","Narrow Gauge"]]
x=np.arange(len(fil_df["Year_in_int"]))
plt.style.use("ggplot")

width=0.2
plt.bar(x-width,select_bmn["Broad Gauge"],align="center",label="Broad",color="red")
plt.bar(x,select_bmn["Metre Gauge"],align="center",label="Metre",color="green")
plt.bar(x+width,select_bmn["Narrow Gauge"],align="center",label="Narrow",color="yellow")
plt.ylabel("three gauges")
plt.xlabel("Year")
plt.title("bar chart")
plt.grid(axis='y')
plt.xticks(x,fil_df["Year_in_int"])
plt.legend()
plt.show()
print("Broad gauge dominented since 2000")

# ============================================================
# 🟡 SCENARIO 4: Pie Chart (Gauge Contribution)
# ============================================================
# 👉 Calculate total sum of:
#     Broad Gauge
#     Metre Gauge
#     Narrow Gauge
# 👉 Store values in a list/structure
# 👉 Plot pie chart
# 👉 Add:
#     Labels
#     Percentage (autopct)
#     Title
# 👉 Save graph inside "graphs" folder
# 👉 Display graph
# 👉 Write observation:
#     Which gauge contributes the most?


s_total=pd.Series({"BGT":df["Broad Gauge"].sum(),
                      "MGT":df["Metre Gauge"].sum(),
                      "NGT":df["Narrow Gauge"].sum()})
#print(s_total)
plt.pie(s_total,labels=["Broad Gauge","Metre Gauge","Narrow Gauge"],
        autopct="%1.1f%%",explode=(0.1,0,0),startangle=180,shadow=True,
        colors=["red", "green","yellow"])
plt.title("percentage contribution")
plt.show()
print("Broad Gauge contributes the most to the total railway network among all gauge types.")

# ============================================================
# 🔴 SCENARIO 5: Advanced Analysis
# ============================================================

# 👉 Create new columns:
#     % Broad Gauge
#     % Metre Gauge
#     % Narrow Gauge

# 👉 Use NumPy to calculate year-to-year growth of Total tracks
# 👉 Add growth as a new column

# 👉 Plot line graph for:
#     Broad Gauge
#     Metre Gauge
#     Total
# 👉 Add title, labels, legend
# 👉 Save graph
# 👉 Display graph

# 👉 Plot stacked bar chart:
#     Broad at bottom
#     Metre on top of Broad
#     Narrow on top of both
# 👉 Add title, labels, legend
# 👉 Rotate X-axis labels
# 👉 Save graph
# 👉 Display graph

# 👉 Identify:
#     Year with highest growth
#     Any declining gauge

# 👉 Final Conclusion:
#     Is railway shifting to a single dominant gauge?
#     Explain in 2–3 lines


df["% Broad Gauge"]=(df["Broad Gauge"]/df["Total"])*100
df["% Metre Gauge"]=(df["Metre Gauge"]/df["Total"])*100
df["% Narrow Gauge"]=(df["Narrow Gauge"]/df["Total"])*100
df["Yearly_growth"]=np.insert(np.diff(df["Total"]),0,0)
print(df["Yearly_growth"])
plt.plot(df["Year_in_int"],df["Narrow Gauge"],label="Narrow Gauge",color="red",marker="o")
plt.plot(df["Year_in_int"],df["Metre Gauge"],label="Metre Gauge",color="orange",marker="o")
plt.plot(df["Year_in_int"],df["Broad Gauge"],label="Broad Gauge",color="green",marker="o")
plt.ylabel("Gauges")
plt.xlabel("Year")
plt.legend()
plt.show()
plt.bar(df["Year_in_int"],df["Narrow Gauge"],label="Narrow Gauge",color="red")
plt.bar(df["Year_in_int"],df["Metre Gauge"],label="Metre Gauge",color="green",bottom=df["Narrow Gauge"])
plt.bar(df["Year_in_int"],df["Broad Gauge"],label="Broad Gauge",color="blue",bottom=df["Metre Gauge"]+df["Narrow Gauge"])
plt.ylabel("Gauges")
plt.xlabel("Year")
plt.legend()
plt.show()
year_highest_growth=df.loc[df["Yearly_growth"].idxmax(),"Year_in_int"]
print(year_highest_growth)
print("Decline years:")
print(df.loc[df["Yearly_growth"] < 0, "Year_in_int"])
print("Yes, the railway system is clearly shifting toward a single dominant gauge that is Broad Gauge.")



# ============================================================
# 📁 Expected Project Structure
# ============================================================
# project1/
# │── railway_gauge_data.csv
# │──  main.py
# │── graphs/
# │     ├── (all saved graphs)
# │── report.pdf
# ============================================================
