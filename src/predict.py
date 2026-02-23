'''
🔵 PHASE 3 — Prediction System
✅ Step 5 — Load model & predict

Create src/predict.py

'''

import joblib

def load_model():
    return joblib.load("models/stay_model.pkl")

def predict(model, data):
    return model.predict(data)