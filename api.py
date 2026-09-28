from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib


# Load trained model
model = joblib.load("linear_regression_model.pkl")

# Load feature columns used during training
feature_columns = joblib.load("feature_columns.pkl")


# Create FastAPI application
app = FastAPI(
    title="Food Delivery Time Prediction API",
    description="Machine Learning API for predicting food delivery time",
    version="1.0"
)


# Input data structure
class DeliveryInput(BaseModel):

    distance: float
    weather: str
    traffic_level: str
    time_of_day: str
    vehicle_type: str
    preparation_time: float
    courier_experience: float


# Home endpoint
@app.get("/")
def home():

    return {
        "message": "Food Delivery Time Prediction API is running"
    }


# Prediction endpoint
@app.post("/predict")
def predict_delivery_time(data: DeliveryInput):

    # Create DataFrame from input
    input_data = pd.DataFrame({
        "Distance_km": [data.distance],
        "Weather": [data.weather],
        "Traffic_Level": [data.traffic_level],
        "Time_of_Day": [data.time_of_day],
        "Vehicle_Type": [data.vehicle_type],
        "Preparation_Time_min": [data.preparation_time],
        "Courier_Experience_yrs": [data.courier_experience]
    })

    # One-hot encode categorical features
    input_data = pd.get_dummies(
        input_data,
        drop_first=True,
        dtype=int
    )

    # Match the exact feature columns used during training
    input_data = input_data.reindex(
        columns=feature_columns,
        fill_value=0
    )

    # Make prediction
    prediction = model.predict(input_data)

    return {
        "predicted_delivery_time": round(float(prediction[0]), 2),
        "unit": "minutes"
    }