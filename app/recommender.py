import pickle
import os

# Load trained model
model_path = os.path.join("models", "recommendation_model.pkl")
model = pickle.load(open(model_path, "rb"))

vehicle_map = {"sedan": 0, "sports": 1, "suv": 2}
location_map = {"urban": 0, "rural": 1}

def recommend_policy(age, vehicle, location, claims):
    vehicle_encoded = vehicle_map.get(vehicle.lower(), 0)
    location_encoded = location_map.get(location.lower(), 0)
    prediction = model.predict([[age, vehicle_encoded, location_encoded, claims]])
    return prediction[0]