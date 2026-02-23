#🔵 PHASE 2 — Machine Learning
#✅ Step 3 — Train model

#Create src/train.py

# Start simple (Random Forest)
'''
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib
from db import fetch_data
from preprocess import preprocess

def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = RandomForestRegressor()
    model.fit(X_train, y_train)

    joblib.dump(model, "E:\\Smart-Hospital-Resource-Forecasting\\models\\stay_model.pkl")

    return model, X_test, y_test

#👉 Goal: working model


# 🔥 THIS PART WAS MISSING
if __name__ == "__main__":
    df = fetch_data(1000)
    X, y = preprocess(df)

    train_model(X, y)
    '''
'''
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
import joblib

def train_model(X, y):

    categorical = ["Age", "Visitors_with_Patient"]
    numeric = []

    preprocessor = ColumnTransformer(
        transformers=[
            ("cat", OneHotEncoder(handle_unknown="ignore"), categorical)
        ]
    )

    pipeline = Pipeline([
        ("prep", preprocessor),
        ("model", RandomForestRegressor())
    ])

    pipeline.fit(X, y)

    joblib.dump(pipeline, "models/stay_model.pkl")

    return pipeline
    '''
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

def train_model(X, y):

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = RandomForestRegressor()
    model.fit(X_train, y_train)

    joblib.dump(model, "E:\\Smart-Hospital-Resource-Forecasting\\models\\stay_model.pkl")
    joblib.dump(X.columns.tolist(),"E:\\Smart-Hospital-Resource-Forecasting\\models\\features.pkl")   # ⭐ IMPORTANT

    print("✅ Model + features saved")

    return model
# 🔥 THIS PART WAS MISSING
from db import fetch_data
from preprocess import preprocess
if __name__ == "__main__":
    df = fetch_data(1000)
    X, y = preprocess(df)
    train_model(X, y)