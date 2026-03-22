from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import joblib
import os

# Create required folder structure
os.makedirs("model/1", exist_ok=True)

# Load dataset
X, y = load_iris(return_X_y=True)

# Train model
model = LogisticRegression(max_iter=200)
model.fit(X, y)

# Save model
joblib.dump(model, "model/1/model.joblib")

print("Model saved at model/1/model.joblib")
