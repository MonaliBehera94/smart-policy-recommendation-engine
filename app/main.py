from fastapi import FastAPI
from app.recommender import recommend_policy
from app.premium_calculator import calculate_premium
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Add this block
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all domains (for local testing)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Smart Policy Recommendation Engine is running!"}

@app.get("/recommend")
def recommend(age: int, vehicle: str, location: str, claims: int):
    policy = recommend_policy(age, vehicle, location, claims)
    premium = calculate_premium(age, vehicle, claims)
    return {
        "recommended_policy": policy,
        "estimated_premium": premium
    }