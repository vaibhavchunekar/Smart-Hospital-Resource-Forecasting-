import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent

model = joblib.load(BASE / "models" / "stay_model.pkl")
features = joblib.load(BASE / "models" / "features.pkl")

st.title("Hospital Stay Prediction")

age = st.slider("Age", 1, 90)
visitors = st.slider("Visitors", 0, 10)

# Create empty dataframe with SAME training columns
input_df = pd.DataFrame(columns=features)
input_df.loc[0] = 0

# fill only known inputs
input_df["Visitors_with_Patient"] = visitors

# example if your preprocess created one-hot Age
col = f"Age_{age}"
if col in input_df.columns:
    input_df[col] = 1

if st.button("Predict"):
    pred = model.predict(input_df)
    st.success(f"Predicted Stay Days: {int(pred[0])}")