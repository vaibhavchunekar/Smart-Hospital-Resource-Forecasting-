# db.py
import mysql.connector
import pandas as pd

def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Indian123#",
        database="hospital"
    )

def fetch_data():
    conn = create_connection()
    df = pd.read_sql("SELECT * FROM hospital_data", conn)
    conn.close()
    return df
