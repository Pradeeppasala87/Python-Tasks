# ============================================================
# STEP 1: IMPORT LIBRARIES
# ============================================================

import numpy as np
import pandas as pd

# ============================================================
# STEP 2: LOAD DATASET
# ============================================================

dataset = pd.read_csv("kc_house_data.csv")
print(dataset.head())

# ============================================================
# STEP 3: FEATURES AND TARGET
# ============================================================

X = dataset[['bedrooms','bathrooms','sqft_living','sqft_lot',
             'floors','condition','grade','sqft_basement',
             'yr_built','yr_renovated']].values

y = dataset['price'].values

print('-'*80)
print(f'Shape of X is {X.shape}')
print(f'Shape of y is {y.shape}')

# ============================================================
# STEP 4: TRAIN-TEST SPLIT
# ============================================================

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=0
)

# ============================================================
# STEP 5: FEATURE SCALING
# ============================================================

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()

X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# ============================================================
# STEP 6: R² SCORE FUNCTION (DIRECT USAGE)
# ============================================================

from sklearn.metrics import r2_score

# ============================================================
# 1. LINEAR REGRESSION
# ============================================================

from sklearn.linear_model import LinearRegression

model_lr = LinearRegression()
model_lr.fit(X_train, y_train)
y_pred_lr = model_lr.predict(X_test)

print("\n-------------------- Linear Regression --------------------")
print("R2 Score:", r2_score(y_test, y_pred_lr))

# ============================================================
# 2. SUPPORT VECTOR REGRESSION (SVR)
# ============================================================

from sklearn.svm import SVR

model_svr = SVR()
model_svr.fit(X_train, y_train)
y_pred_svr = model_svr.predict(X_test)

print("\n-------------------- SVR --------------------")
print("R2 Score:", r2_score(y_test, y_pred_svr))

# ============================================================
# 3. DECISION TREE
# ============================================================

from sklearn.tree import DecisionTreeRegressor

model_dt = DecisionTreeRegressor()
model_dt.fit(X_train, y_train)
y_pred_dt = model_dt.predict(X_test)

print("\n-------------------- Decision Tree --------------------")
print("R2 Score:", r2_score(y_test, y_pred_dt))

# ============================================================
# 4. RANDOM FOREST
# ============================================================

from sklearn.ensemble import RandomForestRegressor

model_rf = RandomForestRegressor()
model_rf.fit(X_train, y_train)
y_pred_rf = model_rf.predict(X_test)

print("\n-------------------- Random Forest --------------------")
print("R2 Score:", r2_score(y_test, y_pred_rf))

# ============================================================
# 5. KNN REGRESSOR
# ============================================================

from sklearn.neighbors import KNeighborsRegressor

model_knn = KNeighborsRegressor(n_neighbors=5)
model_knn.fit(X_train, y_train)
y_pred_knn = model_knn.predict(X_test)

print("\n-------------------- KNN --------------------")
print("R2 Score:", r2_score(y_test, y_pred_knn))

# ============================================================
# 6. RIDGE REGRESSION
# ============================================================

from sklearn.linear_model import Ridge

model_ridge = Ridge()
model_ridge.fit(X_train, y_train)
y_pred_ridge = model_ridge.predict(X_test)

print("\n-------------------- Ridge Regression --------------------")
print("R2 Score:", r2_score(y_test, y_pred_ridge))

# ============================================================
# 7. LASSO REGRESSION
# ============================================================

from sklearn.linear_model import Lasso

model_lasso = Lasso()
model_lasso.fit(X_train, y_train)
y_pred_lasso = model_lasso.predict(X_test)

print("\n-------------------- Lasso Regression --------------------")
print("R2 Score:", r2_score(y_test, y_pred_lasso))
