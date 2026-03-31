import streamlit as st
import pickle

# Page config
st.set_page_config(page_title="Student Predictor", page_icon="📊")

# Load model
model = pickle.load(open("model.pkl", "rb"))

# Title + description
st.title("📊 Student Marks Predictor")
st.markdown("Predict student marks based on study hours and attendance.")

# Inputs
hours = st.slider("Study Hours", 0, 12, 1)
attendance = st.slider("Attendance (%)", 0, 100, 50)

# Prediction
if st.button("🚀 Predict"):
    result = model.predict([[hours, attendance]])
    st.success(f"🎯 Predicted Marks: {result[0]:.2f}")

import matplotlib.pyplot as plt

if st.button("Show Graph"):
    hours_list = list(range(0, 13))
    predictions = [model.predict([[h, attendance]])[0] for h in hours_list]

    plt.plot(hours_list, predictions)
    plt.xlabel("Study Hours")
    plt.ylabel("Predicted Marks")
    plt.title("Marks vs Study Hours")

    st.pyplot(plt)
if hours == 0 or attendance == 0:
    st.warning("⚠️ Please enter valid inputs")
