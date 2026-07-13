import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import RandomizedSearchCV

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

# Hyperparameter values
parameters = {
    "C": [0.01, 0.1, 1, 10, 100],
    "solver": ["liblinear", "lbfgs"]
}

# Random Search
random_search = RandomizedSearchCV(
    estimator=model,
    param_distributions=parameters,
    n_iter=4,
    cv=5,
    scoring="accuracy",
    random_state=42
)

# Train
random_search.fit(X, y)

# Best Results
print("Best Parameters:", random_search.best_params_)
print("Best Score:", random_search.best_score_)
print("Best Model:", random_search.best_estimator_)