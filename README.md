# 🏡 House Price Prediction

Predict house prices using historical property data and machine learning models. This project includes **data analysis, feature engineering, model training**, and a **Streamlit app** for real-time predictions.


## 📌 Problem Statement

House prices are influenced by multiple factors such as location, size, number of rooms, amenities, and economic conditions. Accurate predictions help:

- Buyers identify fair market values.
- Sellers set competitive listing prices.
- Real estate agents and financial institutions make data-driven decisions.

The goal is to build a machine learning system that predicts house prices based on historical data and property features.


## 🔄 Workflow

The typical workflow for building a **House Price Prediction** system includes:

| Step | Description |
|------|-------------|
| **Data Collection & Cleaning** | Compile structured property datasets (e.g., number of bedrooms, bathrooms, location, amenities) and handle missing or inconsistent values. |
| **Exploratory Data Analysis (EDA)** | Visualize trends, examine correlations, and detect outliers. |
| **Feature Engineering** | Create meaningful inputs such as price per square foot, room ratios, or location quality proxies. |
| **Modeling** | Train predictive algorithms such as **Linear Regression**, **Random Forest**, or **Gradient Boosting**. |
| **Evaluation** | Assess model performance using metrics like **RMSE**, **MAE**, and **R²**. |
| **Deployment** | Save the trained pipeline and deploy it through a **Streamlit app** for real-time predictions. |


## 🔢 Dataset

The dataset contains numerical and categorical features:

**Numerical Features:**
- `area`, `bedrooms`, `bathrooms`, `stories`, `parking`, `price`

**Categorical Features:**
- `mainroad`, `guestroom`, `basement`, `hotwaterheating`, `airconditioning`, `prefarea`, `furnishingstatus`


## 📊 Exploratory Data Analysis

- Visualize numerical features vs. price (scatterplots, regression lines, histograms, boxplots)
- Visualize categorical features vs. price (boxplots, countplots)
- Summary statistics for numerical and categorical variables


## 🛠 Feature Engineering

- Create ratios (e.g., bathrooms per bedroom, area per bedroom)
- Encode categorical variables
- Segment houses by price ranges if necessary


## 🤖 Modeling

**Algorithms used:**
- Linear Regression
- Random Forest
- Gradient Boosting

**Metrics:**
- RMSE, MAE, R², Adjusted R², MAPE

**Feature Importance:**
- Random Forest identifies key drivers like **area**, **bathrooms**, **bedrooms**, **air conditioning**, and **furnishing status**.
- Linear Regression coefficients provide interpretable insights for linear relationships.


## 🚀 Deployment

The trained Random Forest pipeline is saved using `joblib`. The project includes a **Streamlit app** for real-time predictions:

```bash
streamlit run House_Price_Prediction_App.py
