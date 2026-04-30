# ============================================================
# 📊 Project Title:IGN Data Analysis
# Analyze IGN dataset using NumPy, Pandas, Matplotlib
# ============================================================


# ============================================================
# 📦 1. Import Required Libraries
# ============================================================
# 👉 Import numpy
# 👉 Import pandas
# 👉 Import matplotlib.pyplot
# 👉 (Optional) Import os for folder creation


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# 📂 3. Load Dataset
# ============================================================
# 👉 Load the dataset using Pandas.
# 👉 Display: ○ First 5 rows (head())
#             ○ Last 5 rows (tail())
#             0 Shape of dataset
# 👉 Display column names

df = pd.read_csv("ign.csv")

print(df.head())
print(df.tail())
print(df.shape)


# ============================================================
# 🟢 SCENARIO 1: Data Loading & Preprocessing
# ============================================================
# 👉 Remove the unnecessary column: ○ "Unnamed: 0" (index column)
# 👉 Check for missing values in:
# 👉 Convert columns:
#   ○ score, genre, platform   
# 👉 Handle missing values:
#   ○ Fill numeric column score with mean
#   ○ Fill categorical column genre with mode
# 👉 Ensure correct data types:
#    ○ score → float
#    ○ release_year, release_month, release_day → integer


# Drop unwanted column
df = df.drop(columns=["Unnamed: 0"], errors="ignore")

# Check missing values
print(df[['score', 'genre', 'platform']].isnull().sum())

# Fill missing values
df['score'] = df['score'].fillna(df['score'].mean())
df['genre'] = df['genre'].fillna(df['genre'].mode()[0])
df['platform'] = df['platform'].fillna(df['platform'].mode()[0])

# Convert data types
df['score'] = df['score'].astype(float)

for col in ['release_year', 'release_month', 'release_day']:
    df[col] = df[col].astype(int)

# Verify
print(df.dtypes)

# ============================================================
# 🟢 SCENARIO 2:  Line Graph (Score Trend) + Save
# ============================================================
# 👉 Group data by release_year. 
# 👉 Calculate average score per year using Pandas
# 👉 Convert results into NumPy arrays. 
# 👉  Plot a line graph: 
#           ○ X-axis → release_year 
#           ○ Y-axis → average score 
# 👉 Add: 
#       ○ Title: "Average Game Score Over Years" 
#       ○ Axis labels
# 👉 Save the graph: plt.savefig("avg_score_trend.png")

yearly_avg = df.groupby('release_year')['score'].mean()

years = yearly_avg.index.to_numpy()
avg_scores = yearly_avg.to_numpy()

plt.figure(figsize=(10,5))
plt.plot(years, avg_scores, marker='o')

plt.title("Average game score over years")
plt.xlabel('release_year')
plt.ylabel('average score')

plt.grid()

plt.savefig("avg_score_trend.png")
plt.show()



# ============================================================
# 🟡 SCENARIO 3:  Filtering + Bar Chart + Save 
# ============================================================

'''
1. Filter dataset where: 
       ○ score > 7 
2. Count number of high-rated games per platform. 
3. Select top 10 platforms using Pandas. 
4. Convert data into NumPy arrays. 
5. Plot a bar chart: 
       ○ X-axis → platform 
       ○ Y-axis → count of games 
6. Rotate x-axis labels for readability. '''


high_rated = df[df['score'] > 7]

platform_counts = high_rated['platform'].value_counts()

top10 = platform_counts.head(10)

platforms = top10.index.to_numpy()
counts = top10.to_numpy()


plt.figure(figsize=(12,6))
plt.bar(platforms, counts)
    
plt.xticks(rotation=45)
plt.title("Top 10 Platforms (Score > 7)")
plt.xlabel("platform")
plt.ylabel("Number of games")

plt.savefig("top_platforms_bar.png")
plt.show()



# ============================================================
# 🟡 SCENARIO 4:  Aggregation + Pie Chart + Save 
# ============================================================

'''
1. Count the number of games per genre. 
2. Select top 5 genres using Pandas. 
3. Prepare labels and values. 
4. Plot a pie chart: 
   ○ Labels → genre 
   ○ Values → count 
5. Add percentage labels (autopct). 
Save the graph: plt.savefig("genre_distribution.png")'''


genre_counts = df['genre'].value_counts()

Top5_genres = genre_counts.head(5)

labels = Top5_genres.index
values = Top5_genres.values

plt.figure(figsize=(7,7))

plt.pie(values, labels=labels, autopct='%1.1f%%')

plt.title("Top 5 Genre Distribution")

plt.savefig("genre_distribution.png")
plt.show()



# ============================================================
# 🔴 SCENARIO 5:  Advanced Analysis + Multiple Graphs 
# ============================================================


'''

Part 1: Feature Engineering 
      1. Create a new column: 
             ○ score_category: 
                 ■ score >= 9 → "Excellent" 
                 ■ 7 <= score < 9 → "Good" 
                 ■ < 7 → "Average" 
2. Convert editors_choice: 
            ○ Y → 1, N → 0 
Part 2: NumPy Analysis 
3. Use NumPy to: 
         ○ Calculate yearly score growth using np.diff() on average yearly scores 
Part 3: Visualizations 
Line Graph
4. Plot trend of: 
             ○  Average score per release_year 
Stacked Bar Chart 
5. Show count of: 
             ○ score_category per release_year 
Histogram 
6. Plot distribution of: 
○ score
Part 4: Save All Graphs 
    plt.savefig("score_trend.png") 
    plt.savefig("score_category_stacked.png") 
    plt.savefig("score_distribution.png") 
Part 5: Insights 
Identify: 
    ● Which years had highest scores 
    ● Whether high scores increased over time 
    ● If editors_choice correlates with high scores  '''

#Part 1: Feature Engineering 

categories = []

for score in df['score']:
    if score >= 9:
        categories.append("Excellent")
    elif score >= 7:
        categories.append("Good")
    else:
        categories.append("Average")

df['score_category'] = categories 

# Convert editors_choice to numeric
df['editors_choice'] = df['editors_choice'].astype(str).str.lower().map({'y': 1, 'n': 0})

# -------------------------------
# Part 2: NumPy Analysis
# -------------------------------

yearly_avg = df.groupby('release_year')['score'].mean().sort_index()

scores_array = yearly_avg.to_numpy()
growth = np.diff(scores_array)

print("Yearly score growth:", growth)

# -------------------------------
# Part 3: Visualizations
# -------------------------------

# 📈 Line Graph
plt.figure(figsize=(10,5))
plt.plot(yearly_avg.index, yearly_avg.values, marker='o')   # FIXED

plt.title("Average Score Trend")
plt.xlabel("Year")
plt.ylabel("Score")

plt.savefig("score_trend.png")
plt.grid()
plt.show()

# -------------------------------
# 📊 Stacked Bar Chart
# -------------------------------

pivot = pd.crosstab(df['release_year'], df['score_category'])

pivot.plot(kind='bar', stacked=True, figsize=(12,6))

plt.title("Score Category per Year")
plt.xlabel("Year")
plt.ylabel("Count")

plt.savefig("score_category_stacked.png")
plt.show()

# -------------------------------
# 📉 Histogram
# -------------------------------

plt.figure(figsize=(8,5))
plt.hist(df['score'], bins=20, edgecolor='black')

plt.title("Score Distribution")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.savefig("score_distribution.png")
plt.show()

# -------------------------------
# Part 5: Insights
# -------------------------------

best_year = yearly_avg.idxmax()
print("Year with highest average score:", best_year)

if growth.mean() > 0:
    print("Scores are increasing over time")
else:
    print("No clear upward trend in scores")

correlation = df['editors_choice'].corr(df['score'])
print("Correlation between editors choice and score:", correlation)

if correlation > 0.5:
    print("Strong positive correlation")
elif correlation > 0.2:
    print("Moderate correlation")
else:
    print("Weak or no correlation")













            
