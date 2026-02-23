#Step 4 — Evaluate model

#Create src/evaluate.py

from sklearn.metrics import mean_absolute_error, r2_score

def evaluate(model, X_test, y_test):
    pred = model.predict(X_test)

    print("MAE:", mean_absolute_error(y_test, pred))
    print("R2:", r2_score(y_test, pred))
'''

👉 Goal: know performance
'''
