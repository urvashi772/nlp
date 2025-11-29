import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("eligibility_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

st.title("Loan & Credit Card Eligibility Predictor")

income = st.number_input("Enter Income", min_value=0)
score = st.number_input("Enter Credit Score", min_value=300, max_value=900)

if st.button("Check Eligibility"):
    data = np.array([[income, score]])
    scaled = scaler.transform(data)
    pred = model.predict(scaled)[0]

    if pred == 0:
        st.error("❌ Person is NOT eligible for any service.")
    elif pred == 1:
        st.success("💳 Person is Eligible for **Credit Card Only**")
    elif pred == 2:
        st.success("🏦 Person is Eligible for **Loan Only**")
    elif pred == 3:
        st.success("💳🏦 Person is Eligible for **Both Loan & Credit Card**")
