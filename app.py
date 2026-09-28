import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("linear_regression_model.pkl")
feature_columns = joblib.load("feature_columns.pkl")


# Prediction function
def predict_delivery_time(
    distance,
    weather,
    traffic_level,
    time_of_day,
    vehicle_type,
    preparation_time,
    courier_experience
):
    
    input_data = pd.DataFrame({
        "Distance_km": [distance],
        "Weather": [weather],
        "Traffic_Level": [traffic_level],
        "Time_of_Day": [time_of_day],
        "Vehicle_Type": [vehicle_type],
        "Preparation_Time_min": [preparation_time],
        "Courier_Experience_yrs": [courier_experience]
    })

    # Encode categorical columns
    input_data = pd.get_dummies(
        input_data,
        drop_first=True,
        dtype=int
    )

    # Match training columns
    input_data = input_data.reindex(
        columns=feature_columns,
        fill_value=0
    )

    # Predict
    prediction = model.predict(input_data)

    return prediction[0]


# Page configuration
st.set_page_config(
    page_title="Food Delivery Time Predictor",
    page_icon="🚚",
    layout="centered"
)

# Title
st.title("🚚 Food Delivery Time Predictor")
st.write("Predict estimated food delivery time using machine learning.")

st.divider()

# User inputs
distance = st.number_input(
    "Distance (km)",
    min_value=0.1,
    max_value=100.0,
    value=8.0
)

weather = st.selectbox(
    "Weather",
    ["Clear", "Foggy", "Rainy", "Snowy", "Windy"]
)

traffic_level = st.selectbox(
    "Traffic Level",
    ["Low", "Medium", "High"]
)

time_of_day = st.selectbox(
    "Time of Day",
    ["Morning", "Afternoon", "Evening", "Night"]
)

vehicle_type = st.selectbox(
    "Vehicle Type",
    ["Bike", "Scooter", "Car"]
)

preparation_time = st.number_input(
    "Preparation Time (minutes)",
    min_value=1,
    max_value=120,
    value=20
)

courier_experience = st.number_input(
    "Courier Experience (years)",
    min_value=0.0,
    max_value=30.0,
    value=2.0
)

st.divider()

# Prediction button
if st.button("Predict Delivery Time", type="primary"):

    prediction = predict_delivery_time(
        distance,
        weather,
        traffic_level,
        time_of_day,
        vehicle_type,
        preparation_time,
        courier_experience
    )

    st.success(
        f"Estimated Delivery Time: {prediction:.2f} minutes"
    )