# ============================================================
# STEP 1: IMPORT LIBRARIES (TOOLS WE NEED)
# ============================================================

import numpy as np          
import pandas as pd        

# ============================================================
# STEP 2: LOAD DATASET (INPUT DATA)
# ============================================================

# Load dataset into a DataFrame (table structure)
dataset = pd.read_csv("kc_house_data.csv")

# View first few rows → helps understand columns & values
print(dataset.head())


# ============================================================
# STEP 3: DEFINE FEATURES (X) AND TARGET (y)
# ============================================================

# FEATURES = input variables (what we use to predict price)
X = dataset[['bedrooms','bathrooms','sqft_living','sqft_lot',
             'floors','condition','grade','sqft_basement',
             'yr_built','yr_renovated']].values

# TARGET = output variable (what we want to predict)
y = dataset['price'].values

# Check dataset size → rows (samples), columns (features)
print('-'*80)
print(f'Shape of X is {X.shape}')  # Example: (21613, 10)
print(f'Shape of y is {y.shape}')  # Example: (21613,)


# ============================================================
# STEP 4: SPLIT DATA (TRAINING vs TESTING)
# ============================================================

# WHY?
# Train data → model learns patterns
# Test data → model is evaluated on unseen data

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,     # 20% test data
    random_state=0     # ensures same split every time
)


# ============================================================
# STEP 5: FEATURE SCALING (NORMALIZATION)
# ============================================================

# WHY?
# Some models (SVR, KNN) depend on distance → scaling is important

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()

# Learn scaling from training data ONLY
X_train = sc.fit_transform(X_train)

# Apply same scaling to test data
X_test = sc.transform(X_test)

# ============================================================
# STEP 6: MODEL EVALUATION FUNCTION
# ============================================================

# R² Score → measures how well predictions match actual values
from sklearn.metrics import r2_score

def evaluate(name, y_test, y_pred):
    """
    Prints model performance
    R² score range:
    1   = perfect prediction
    0   = average prediction
    < 0 = very bad model
    """
    print('\n'+'-'*20 + f' {name} ' + '-'*20)
    print("Accuracy (R2 Score):", "{:.2f}".format(r2_score(y_test, y_pred)))


# ============================================================
# STEP 7: APPLY DIFFERENT MACHINE LEARNING MODELS
# ============================================================

# ------------------------------------------------------------
# 1. LINEAR REGRESSION
# ------------------------------------------------------------
# Idea: price = m1*x1 + m2*x2 + ... + c
# Assumes straight-line relationship

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)        # Learn patterns
y_pred = model.predict(X_test)     # Predict

evaluate("Linear Regression", y_test, y_pred)


# ------------------------------------------------------------
# 2. SUPPORT VECTOR REGRESSION (SVR)
# ------------------------------------------------------------
# Idea: finds best boundary within a margin (handles non-linear data)

from sklearn.svm import SVR

model = SVR()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

evaluate("Support Vector Regression", y_test, y_pred)


# ------------------------------------------------------------
# 3. DECISION TREE
# ------------------------------------------------------------
# Idea: splits data like a flowchart (if-else rules)

from sklearn.tree import DecisionTreeRegressor

model = DecisionTreeRegressor()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

evaluate("Decision Tree", y_test, y_pred)


# ------------------------------------------------------------
# 4. RANDOM FOREST
# ------------------------------------------------------------
# Idea: combines multiple trees → reduces overfitting

from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

evaluate("Random Forest", y_test, y_pred)


# ------------------------------------------------------------
# 5. K-NEAREST NEIGHBORS (KNN)
# ------------------------------------------------------------
# Idea: predicts based on similar nearby data points

from sklearn.neighbors import KNeighborsRegressor

model = KNeighborsRegressor(n_neighbors=5)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

evaluate("KNN", y_test, y_pred)


# ------------------------------------------------------------
# 6. RIDGE REGRESSION
# ------------------------------------------------------------
# Idea: linear model + penalty → avoids overfitting

from sklearn.linear_model import Ridge

model = Ridge()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# ==========================================
# 7. Lasso Regression
# ==========================================
from sklearn.linear_model import Lasso
model = Lasso()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
evaluate("Lasso Regression", y_test, y_pred)










evaluate("Ridge Regression", y_test, y_pred)
