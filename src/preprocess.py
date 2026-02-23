# preprocess.py
import pandas as pd

mapping = {
    "0-10":5, "11-20":15, "21-30":25,
    "31-40":35, "41-50":45
}

def preprocess(df):
    df["Stay_days"] = df["Stay"].map(mapping)

    df = pd.get_dummies(df, drop_first=True)

    X = df.drop("Stay_days", axis=1)
    y = df["Stay_days"]

    return X, y
