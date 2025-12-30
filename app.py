import streamlit as st
import pandas as pd
import pickle

with open("heart_disease_model.pkl", "rb") as file:
    model = pickle.load(file)

st.set_page_config(page_title="Heart Disease Prediction", layout="centered")
st.title("❤️ Heart Disease Prediction App")

st.write("Enter patient details to predict heart disease.")


age = st.number_input("Age", 1, 120, 45)
sex = st.selectbox("Sex", ["M", "F"])
chest_pain = st.selectbox("Chest Pain Type", ["Non-Anginal Pain" , "Atypical Angina" , "Typical Angina", "Asymptomatic"])
resting_bp = st.number_input("Resting Blood Pressure", 80, 200, 120)
cholesterol = st.number_input("Cholesterol", 100, 400, 200)
fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
resting_ecg = st.selectbox("Resting ECG", ["Normal", "ST", "LVH"])
max_hr = st.number_input("Max Heart Rate", 60, 220, 150)
exercise_angina = st.selectbox("Exercise Induced Angina", ["NO", "YES"])
oldpeak = st.number_input("Oldpeak (ST depression)", 0.0, 6.0, 1.0)
st_slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"])

input_dict = {
    "Age": age,
    "RestingBP": resting_bp,
    "Cholesterol": cholesterol,
    "FastingBS": fasting_bs,
    "MaxHR": max_hr,
    "Oldpeak": oldpeak
}

df_input = pd.DataFrame([input_dict])

df_input["Sex_M"] = 1 if sex == "M" else 0
df_input["ExerciseAngina_Y"] = 1 if exercise_angina == "YES" else 0

df_input["ChestPainType_ATA"] = 1 if chest_pain == "Atypical Angina" else 0
df_input["ChestPainType_NAP"] = 1 if chest_pain == "Non-Anginal Pain" else 0
df_input["ChestPainType_TA"] = 1 if chest_pain == "Typical Angina" else 0

df_input["RestingECG_ST"] = 1 if resting_ecg == "ST" else 0
df_input["RestingECG_LVH"] = 1 if resting_ecg == "LVH" else 0

df_input["ST_Slope_Flat"] = 1 if st_slope == "Flat" else 0
df_input["ST_Slope_Up"] = 1 if st_slope == "Up" else 0

model_features = model.feature_names_in_

for col in model_features:
    if col not in df_input.columns:
        df_input[col] = 0

df_input = df_input[model_features]

if st.button("Predict"):
    result = model.predict(df_input)[0]

    if result == 1:
        st.error(" High risk of Heart Disease!!")
    else:
        st.success(" Low risk of Heart Disease.")
