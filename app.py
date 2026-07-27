import streamlit as st
import pandas as pd
import joblib

# Page Configuration
st.set_page_config(
    page_title="Car Price Prediction",
    layout="centered"
)

# Load Model
model = joblib.load("car_price_model.pkl")

# Load Label Encoders
label_encoders = joblib.load("label_encoders.pkl")

# Load Dataset
train_df = pd.read_csv("Cap_Training_Data_2025.csv")

st.title("Indian Pre-Owned Car Price Prediction")

st.write(
    "Enter the details of a used car to predict its estimated selling price."
)
maker = st.selectbox(
    "Maker",
    sorted(train_df["Maker"].dropna().astype(str).unique())
)

model_name = st.selectbox(
    "Model",
    sorted(train_df["model"].dropna().astype(str).unique())
)

location = st.selectbox(
    "Location",
    sorted(train_df["Location"].dropna().astype(str).unique())
)

distance = st.number_input(
    "Distance (km)",
    min_value=0
)

owner_type = st.selectbox(
    "Owner Type",
    sorted(train_df["Owner Type"].dropna().astype(str).unique())
)

manufacture_year = st.number_input(
    "Manufacture Year",
    min_value=1990,
    max_value=2025,
    value=2020
)

age = st.number_input(
    "Age of Car",
    min_value=0,
    max_value=40,
    value=5
)

engine_displacement = st.number_input(
    "Engine Displacement (cc)",
    min_value=500,
    max_value=7000,
    value=1200
)

engine_power = st.number_input(
    "Engine Power (HP)",
    min_value=30,
    max_value=1000,
    value=100
)

body_type = st.selectbox(
    "Body Type",
    sorted(train_df["body_type"].dropna().astype(str).unique())
)

rating = st.slider(
    "Vroom Audit Rating",
    1.0,
    5.0,
    3.0
)

transmission = st.selectbox(
    "Transmission",
    sorted(train_df["transmission"].dropna().astype(str).unique())
)

door_count = st.number_input(
    "Door Count",
    min_value=2,
    max_value=6,
    value=4
)

seat_count = st.number_input(
    "Seat Count",
    min_value=2,
    max_value=10,
    value=5
)

fuel_type = st.selectbox(
    "Fuel Type",
    sorted(train_df["fuel_type"].dropna().astype(str).unique())
)
if st.button("Predict Price"):

    input_data = {
    "Maker": maker,
    "model": model_name,
    "Location": location,
    "Distance ": distance,
    "Owner Type": owner_type,
    "manufacture_year": manufacture_year,
    "Age of car": age,
    "engine_displacement": engine_displacement,
    "engine_power": engine_power,
    "body_type": body_type,
    "Vroom Audit Rating": rating,
    "transmission": transmission,
    "door_count": door_count,
    "seat_count": seat_count,
    "fuel_type": fuel_type
    }

    input_df = pd.DataFrame([input_data])
    categorical_columns = [
    "Maker",
    "model",
    "Location",
    "Owner Type",
    "body_type",
    "transmission",
    "fuel_type"
    ]

    for col in categorical_columns:

        input_df[col] = label_encoders[col].transform(
            input_df[col].astype(str)
        )
    
    prediction = model.predict(input_df)

    st.success(
    f"Estimated Car Price: ₹ {prediction[0]:,.0f}"
    )