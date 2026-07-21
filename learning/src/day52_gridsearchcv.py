import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV

# Load dataset
df = pd.read_csv("../data/online_retail_cleaned.csv")

print("Dataset Loaded Successfully!")

# Create target column
df["Fraud"] = (df["Quantity"] > 20).astype(int)

# Features
X = df[["Quantity", "UnitPrice"]]

# Target
y = df["Fraud"]

# Model
model = LogisticRegression(max_iter=1000)

# Hyperparameters to test
parameters = {
    "C": [0.1, 1, 10]
}

# Grid Search
grid = GridSearchCV(
    estimator=model,
    param_grid=parameters,
    cv=5,
    scoring="accuracy"
)

# Train
grid.fit(X, y)

# Results
print("Best Parameter:", grid.best_params_)
print("Best Score:", grid.best_score_)
print("Best Model:", grid.best_estimator_)