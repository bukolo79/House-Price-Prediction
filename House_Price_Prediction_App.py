# -*- coding: utf-8 -*-
"""
Created on Sun Sep 14 20:15:51 2025

@author: Oluwaseun Adeyemi
"""

import joblib 
import streamlit as st
import pandas as pd
import numpy as np

# -----------------------------
# 🛠 Page Config
# -----------------------------
st.set_page_config(page_title="House Price Prediction App", page_icon="🏠", layout="centered")

# 🔧 Remove extra top padding
st.markdown("""
    <style>
        .block-container {
            padding-top: 1rem;
        }
    </style>
""", unsafe_allow_html=True)

# -----------------------------
# 🎯 App Title & Introduction
# -----------------------------
st.title("🏠 House Price Prediction App")
st.markdown("""
Welcome to the **House Price Prediction App**!  
This app uses a trained **Random Forest Machine Learning model** to estimate house prices based on property features.  

💡 **How to use this app**:
1. Enter the property details in the form (left sidebar).  
2. Click on **Predict House Price**.  
3. Instantly see the predicted house price 💰.  
""")

# -----------------------------
# 📋 Input Form (Sidebar)
# -----------------------------
st.sidebar.header("Enter House Details")

area = st.sidebar.number_input("🏡 Area (sq ft)", min_value=500, max_value=20000, value=3000)
bedrooms = st.sidebar.number_input("🛏 Bedrooms", min_value=1, max_value=10, value=3)
bathrooms = st.sidebar.number_input("🛁 Bathrooms", min_value=1, max_value=5, value=2)
stories = st.sidebar.number_input("🏢 Stories", min_value=1, max_value=4, value=2)
parking = st.sidebar.number_input("🚗 Parking Spots", min_value=0, max_value=5, value=1)

mainroad = st.sidebar.selectbox("🛣 Main Road", ["yes", "no"])
guestroom = st.sidebar.selectbox("🛋 Guest Room", ["yes", "no"])
basement = st.sidebar.selectbox("🏗 Basement", ["yes", "no"])
hotwaterheating = st.sidebar.selectbox("🔥 Hot Water Heating", ["yes", "no"])
airconditioning = st.sidebar.selectbox("❄ Air Conditioning", ["yes", "no"])
prefarea = st.sidebar.selectbox("🌳 Preferred Area", ["yes", "no"])
furnishingstatus = st.sidebar.selectbox("🛋 Furnishing Status", ["furnished", "semi-furnished", "unfurnished"])

# -----------------------------
# 🧾 Create DataFrame for Prediction
# -----------------------------
input_data = pd.DataFrame({
    'area': [area],
    'bedrooms': [bedrooms],
    'bathrooms': [bathrooms],
    'stories': [stories],
    'parking': [parking],
    'mainroad': [mainroad],
    'guestroom': [guestroom],
    'basement': [basement],
    'hotwaterheating': [hotwaterheating],
    'airconditioning': [airconditioning],
    'prefarea': [prefarea],
    'furnishingstatus': [furnishingstatus]
})

st.subheader("📊 Input Summary")
st.write(input_data)

# -----------------------------
# 🔮 Prediction
# -----------------------------
model = joblib.load("random_forest_pipeline.pkl")

if st.button("🚀 Predict House Price"):
    log_price = model.predict(input_data)[0]
    predicted_price = np.exp(log_price)  # convert back from log scale

    st.success(f"💰 **Predicted House Price:** ${predicted_price:,.2f}")
    st.balloons()
