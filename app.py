import streamlit as st
import pandas as pd
import joblib

model = joblib.load("best_model.pkl")

st.title(" Loan Payment Difficulty Prediction")

st.write("Enter the applicant details below:")

features = model.feature_names_in_

data = {}

for feature in features:
    data[feature] = st.number_input(
        feature,
        value=0.0
    )

if st.button("Predict"):

    X = pd.DataFrame([data])

    prediction = model.predict(X)[0]

    if prediction == 1:
        st.error("⚠️ Payment Difficulty")
    else:
        st.success("✅ No Payment Difficulty")