#=====================================================================
# BANK FRAUD DETECTION - OPTIMIZED VERSION
#=====================================================================

#=====================================================================
# Import Libraries
#=====================================================================

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import accuracy_score

#=====================================================================
# Load Dataset
#=====================================================================

df = pd.read_csv("bank_transactions_data_2.csv")

#=====================================================================
# Display Basic Information
#=====================================================================

print("\nFirst 5 Rows")
print(df.head())

print("\nDataset Shape")
print(df.shape)

print("\nColumns")
print(df.columns)

#=====================================================================
# Handle Missing Values
#=====================================================================

# Numeric columns

numeric_cols = df.select_dtypes(include=np.number).columns

for col in numeric_cols:

    df[col] = df[col].fillna(df[col].mean())

# Categorical columns

categorical_cols = df.select_dtypes(
    include=['object', 'string']
).columns

for col in categorical_cols:

    df[col] = df[col].fillna(df[col].mode()[0])

#=====================================================================
# Detect Target Column
#=====================================================================

possible_targets = [
    'Fraud',
    'fraud',
    'IsFraud',
    'is_fraud',
    'Class',
    'class'
]

target_column = None

for col in possible_targets:

    if col in df.columns:

        target_column = col

        break

if target_column is None:

    print("Fraud column not found")
    exit()

print("\nTarget Column :", target_column)

#=====================================================================
# Convert Target Values
#=====================================================================

if df[target_column].dtype == 'object':

    df[target_column] = df[target_column].replace({
        'Yes':1,
        'No':0,
        'Fraud':1,
        'Normal':0
    })

#=====================================================================
# Encode Categorical Data
#=====================================================================

encoder = LabelEncoder()

categorical_cols = df.select_dtypes(
    include=['object', 'string']
).columns

for col in categorical_cols:

    df[col] = encoder.fit_transform(df[col])

#=====================================================================
# Feature Selection
#=====================================================================

X = df.drop(target_column, axis=1)

y = df[target_column]

#=====================================================================
# Reduce Dataset Size (IMPORTANT)
#=====================================================================

# Take only 5000 rows for fast execution

X = X.head(5000)

y = y.head(5000)

#=====================================================================
# Feature Scaling
#=====================================================================

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

#=====================================================================
# Train Test Split
#=====================================================================

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled,
    y,
    test_size=0.2,
    random_state=42
)

#=====================================================================
# KNN MODEL
#=====================================================================

print("\n==========================")
print("KNN CLASSIFIER")
print("==========================")

knn_model = KNeighborsClassifier(
    n_neighbors=3
)

knn_model.fit(X_train, y_train)

knn_predictions = knn_model.predict(X_test)

knn_accuracy = accuracy_score(
    y_test,
    knn_predictions
)

print("KNN Accuracy :", knn_accuracy)

#=====================================================================
# LOGISTIC REGRESSION
#=====================================================================

print("\n==========================")
print("LOGISTIC REGRESSION")
print("==========================")

lr_model = LogisticRegression(
    max_iter=500
)

lr_model.fit(X_train, y_train)

lr_predictions = lr_model.predict(X_test)

lr_accuracy = accuracy_score(
    y_test,
    lr_predictions
)

print("Logistic Regression Accuracy :", lr_accuracy)

#=====================================================================
# Model Comparison
#=====================================================================

print("\n==========================")
print("MODEL COMPARISON")
print("==========================")

print("KNN Accuracy                 :", knn_accuracy)

print("Logistic Regression Accuracy :", lr_accuracy)

if knn_accuracy > lr_accuracy:

    print("\nBest Model : KNN")

else:

    print("\nBest Model : Logistic Regression")

#=====================================================================
# Predict Single Transaction
#=====================================================================

sample_transaction = X_scaled[0:1]

prediction = knn_model.predict(
    sample_transaction
)

print("\n==========================")
print("PREDICTION")
print("==========================")

if prediction[0] == 1:

    print("Fraud Transaction")

else:

    print("Normal Transaction")

print("\nProject Completed Successfully")
