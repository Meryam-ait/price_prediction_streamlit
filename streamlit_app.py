import streamlit as st
import pickle
import numpy as np
import xgboost as xgb
# Load the saved model
# Load the model from the JSON file
booster = xgb.Booster()
booster.load_model('xgb_regressor_model.json')

# Re-create the XGBRegressor from the loaded Booster
xgb_regressor = xgb.XGBRegressor()
xgb_regressor._Booster = booster



# Load LabelEncoders and Scaler
with open("label_encoders.pkl", "rb") as file:
    label_encoders = pickle.load(file)
with open("scaler.pkl", "rb") as file:
    scaler = pickle.load(file)

st.title("Car Price Prediction App")
st.markdown("Enter car details to predict its price.")

# Collect user input
abtest = st.text_input("AB Test")
vehicle_type = st.text_input("Vehicle Type")
gearbox = st.text_input("Gearbox")
model = st.text_input("Model")
fuel_type = st.text_input("Fuel Type")
brand = st.text_input("Brand")
not_repaired_damage = st.text_input("Not Repaired Damage")
kilometer = st.number_input("Kilometer Driven", min_value=0.0, value=50000.0)
power_ps = st.number_input("Power (PS)", min_value=0.0, value=100.0)
car_age = st.number_input("Car Age (years)", min_value=0.0, value=5.0)

# Prediction button
if st.button("Predict"):
    try:
        # Encode categorical variables
        encoded_inputs = [
            label_encoders["abtest"].transform([abtest])[0],
            label_encoders["vehicleType"].transform([vehicle_type])[0],
            label_encoders["gearbox"].transform([gearbox])[0],
            label_encoders["model"].transform([model])[0],
            label_encoders["fuelType"].transform([fuel_type])[0],
            label_encoders["brand"].transform([brand])[0],
            label_encoders["notRepairedDamage"].transform([not_repaired_damage])[0],
        ]

        # Normalize numerical variables
        numerical_inputs = scaler.transform([[kilometer, power_ps, car_age]])

        # Combine encoded and numerical features
        features = np.array([encoded_inputs + numerical_inputs[0].tolist()])

        # Make prediction
        prediction = xgb_regressor.predict(features)
        st.success(f"Predicted Price: {prediction[0]:.2f}")
    except Exception as e:
        st.error(f"Error: {e}")
