🏥 Smart Hospital Resource Forecasting System

End-to-end healthcare analytics and machine learning system to forecast hospital bed occupancy, patient stay duration, and resource demand using MySQL, Python, and Streamlit.

This project demonstrates real-world data engineering, machine learning, and deployment skills by transforming raw hospital data into actionable insights for hospital administrators.

📌 Problem Statement

Hospitals frequently face:

Bed shortages

Overcrowding

Inefficient resource allocation

Long patient waiting times

Without accurate forecasting, planning staff, beds, and equipment becomes reactive instead of proactive.

✅ Solution

This system:

Extracts hospital data from MySQL

Cleans and preprocesses records (ETL pipeline)

Trains ML models to predict patient stay duration

Forecasts bed occupancy and resource requirements

Provides an interactive Streamlit dashboard for real-time decisions

🛠 Tech Stack

Python – Pandas, NumPy, Scikit-learn

MySQL – Database & SQL queries

Streamlit – Dashboard deployment

Matplotlib / Seaborn – Visualization

Machine Learning – Regression & Classification models

🚀 Key Features

MySQL database connectivity

Automated preprocessing pipeline

Multiple ML models:

Logistic Regression

Random Forest

Decision Tree

Model comparison & evaluation:

Accuracy

Confusion Matrix

ROC Curve

Bed occupancy forecasting

Interactive web dashboard

Modular production-style codebase

📊 Business Impact

Improves bed utilization planning

Reduces patient waiting time

Supports data-driven hospital management

Enables predictive healthcare analytics

🧠 Skills Demonstrated

This project showcases:

Data Engineering (ETL, SQL, pipelines)

Machine Learning modeling & evaluation

Feature engineering

Forecasting techniques

Dashboard development

End-to-end deployment

Healthcare analytics use case

👉 Relevant for roles: Data Analyst | Data Scientist | ML Engineer | BI Developer

📁 Project Structure
Smart-Hospital-Resource-Forecasting/
│
├── data/          # datasets
├── src/           # preprocessing + models
├── models/        # saved models
├── notebooks/     # experiments
├── app.py         # Streamlit dashboard
├── requirements.txt
└── README.md

▶️ How to Run
git clone <repo-url>
cd Smart-Hospital-Resource-Forecasting
pip install -r requirements.txt
streamlit run app.py

📷 Dashboard Preview

(Add screenshots here)

📜 License

Licensed under MIT License.
