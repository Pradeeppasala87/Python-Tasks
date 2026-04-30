# Import required libraries
from random import randint
from sklearn.linear_model import LinearRegression

# Set limits
TRAIN_SET_LIMIT = 1000
TRAIN_SET_COUNT = 100

# Create empty lists
TRAIN_INPUT = []
TRAIN_OUTPUT = []

# Generate dataset
for i in range(TRAIN_SET_COUNT):
    a = randint(0, TRAIN_SET_LIMIT)
    b = randint(0, TRAIN_SET_LIMIT)
    c = randint(0, TRAIN_SET_LIMIT)
    d = randint(0, TRAIN_SET_LIMIT)

    # Function: y = 7a + 3b + 4c + 9d
    op = (7*a) + (3*b) + (4*c) + (9*d)

    TRAIN_INPUT.append([a, b, c, d])
    TRAIN_OUTPUT.append(op)

# Create Linear Regression model
model = LinearRegression()

# Train model
model.fit(TRAIN_INPUT, TRAIN_OUTPUT)

# Test data
X_TEST = [[10, 20, 30, 40]]

# Predict output
result = model.predict(X_TEST)

# Print results
print("Predicted Output:", result)
print("Learned Coefficients:", model.coef_)
