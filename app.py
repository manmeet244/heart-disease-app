import streamlit as st
import pandas as pd
import joblib

model = joblib.load("model.pkl")

st.title("Cardiovascular Disease Risk Predictor")

st.write("### Fill patient details below")

# 🔥 Manual inputs (NO LOOP = NO BUGS)

gender = st.selectbox("Gender", ["Female", "Male"])
age = st.number_input("Age", 20, 100, 40)
smoker = st.selectbox("Current Smoker", ["No", "Yes"])
cigs = st.number_input("Cigarettes per Day", 0, 50, 0)
bpmeds = st.selectbox("BP Medication", ["No", "Yes"])
stroke = st.selectbox("Previous Stroke", ["No", "Yes"])
hypertension = st.selectbox("Hypertension", ["No", "Yes"])
diabetes = st.selectbox("Diabetes", ["No", "Yes"])

sysBP = st.number_input("Systolic BP", 80, 250, 120)
diaBP = st.number_input("Diastolic BP", 50, 150, 80)
chol = st.number_input("Cholesterol", 100, 400, 200)
bmi = st.number_input("BMI", 10.0, 50.0, 25.0)
glucose = st.number_input("Glucose", 50, 400, 100)

# 🔥 Convert to model format
data = pd.DataFrame([{
    "male": 1 if gender == "Male" else 0,
    "age": age,
    "currentSmoker": 1 if smoker == "Yes" else 0,
    "cigsPerDay": cigs,
    "BPMeds": 1 if bpmeds == "Yes" else 0,
    "prevalentStroke": 1 if stroke == "Yes" else 0,
    "prevalentHyp": 1 if hypertension == "Yes" else 0,
    "diabetes": 1 if diabetes == "Yes" else 0,
    "sysBP": sysBP,
    "diaBP": diaBP,
    "totChol": chol,
    "BMI": bmi,
    "glucose": glucose
}])

# 🔥 Prediction
if st.button("Predict"):
    prob = model.predict_proba(data)[0][1]

    st.write(f"### Risk Probability: {prob:.2f}")

    if prob > 0.5:
        st.error("⚠️ High Risk of Heart Disease")
    else:
        st.success("✅ Low Risk")
