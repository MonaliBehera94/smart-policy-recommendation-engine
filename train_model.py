import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
import pickle
import os

# Ensure models folder exists
if not os.path.exists("models"):
    os.makedirs("models")

# Load data
data = pd.read_csv("data/insurance_profiles.csv")

# Encode categorical features
le_vehicle = LabelEncoder()
le_location = LabelEncoder()
data["vehicle_type"] = le_vehicle.fit_transform(data["vehicle_type"])
data["location"] = le_location.fit_transform(data["location"])

# Features and target
X = data[["age", "vehicle_type", "location", "claim_history"]]
y = data["recommended_policy"]

# Train model
model = DecisionTreeClassifier()
model.fit(X, y)

# Save model
pickle.dump(model, open("models/recommendation_model.pkl", "wb"))

print("Model trained and saved.")