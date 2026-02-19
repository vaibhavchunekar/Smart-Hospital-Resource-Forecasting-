# 🏥 Smart Hospital Resource Forecasting System

**End-to-end healthcare analytics and machine learning system to forecast hospital bed occupancy and patient stay duration using MySQL, Python, and Streamlit.**

Smart Hospital Resource Forecasting System transforms raw hospital data into insights and predictions that help hospital administrators make informed operational decisions.

---

## 🧠 Problem Statement

Hospitals often struggle with:

- Bed shortages
- Overcrowding
- Inefficient resource allocation
- Long waiting times

Accurate forecasting of patient stay and admissions can help administrators plan staffing, beds, and equipment more effectively.

---

## 💡 Solution Overview

This project:

- Extracts data from a MySQL database
- Cleans and preprocesses records
- Trains machine learning models to predict patient stay duration
- Forecasts resource requirements
- Provides an interactive Streamlit dashboard for decision support

---

## 🛠 Tech Stack

- **Python** – Pandas, NumPy, Scikit-Learn  
- **MySQL** – Database interaction and ETL  
- **Streamlit** – Interactive dashboard  
- **Matplotlib / Seaborn** – Visualization  

---

## 🚀 Key Features

- MySQL database connectivity  
- Automated data preprocessing  
- Multiple ML models:
  - Logistic Regression
  - Random Forest
  - Decision Tree  
- Model evaluation (accuracy, ROC curve, confusion matrix)  
- Interactive dashboard for prediction and visualization  
- Modular, production-style code structure  

---

## 📊 Business Impact

This system can:

- Improve bed utilization planning  
- Reduce patient waiting times  
- Support data-driven hospital management  
- Enable predictive healthcare analytics

---

## 📁 Project Structure
Smart-Hospital-Resource-Forecasting/
│
├── data/ # input datasets
├── src/ # preprocessing + models
├── models/ # saved machine learning models
├── notebooks/ # exploratory analysis
├── app.py # Streamlit dashboard
├── requirements.txt
└── README.md

---

## ▶️ How to Run

```bash
git clone https://github.com/vaibhavchunekar/Smart-Hospital-Resource-Forecasting-
cd Smart-Hospital-Resource-Forecasting-
pip install -r requirements.txt
streamlit run app.py


---



