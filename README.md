# Car Price Prediction App

This is a **Streamlit** application designed to predict the price of a car based on various features such as model, brand, fuel type, power (PS), kilometers driven, and more. The app uses an **XGBoost** regressor model to make accurate price predictions, which is trained using historical data of car listings.

## Features

- **User Input**: The app allows users to input car details such as:
  - AB Test
  - Vehicle Type
  - Gearbox Type
  - Model
  - Fuel Type
  - Brand
  - Not Repaired Damage
  - Kilometer Driven
  - Power (PS)
  - Car Age
  
- **Car Price Prediction**: After the user provides the car details, the app will predict the car price using a pre-trained **XGBoost** regressor model. The prediction is displayed on the screen.

- **Machine Learning Model**: The app uses a trained XGBoost model that has been saved as a `.pkl` file. The model has been optimized for CPU usage.

## Installation

### Requirements

To run this app locally, you need to install the following dependencies:

- `streamlit`
- `xgboost`
- `numpy`
- `scikit-learn`

You can install these dependencies by running:

```bash
pip install -r requirements.txt
