import streamlit as st
import pickle
import matplotlib.pyplot as plt

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Student Marks Predictor",
    page_icon="📊",
    layout="centered"
)

# -----------------------------
# Load Model
# -----------------------------
model = pickle.load(open("model.pkl", "rb"))

# -----------------------------
# Title & Description
# -----------------------------
st.title("📊 Student Marks Predictor")
st.markdown("Predict student marks based on study hours and attendance.")

# -----------------------------
# Inputs
# -----------------------------
hours = st.slider("📚 Study Hours", 0, 12, 1)
attendance = st.slider("📅 Attendance (%)", 0, 100, 50)

# -----------------------------
# Prediction
# -----------------------------
if st.button("🚀 Predict"):
    if hours == 0 or attendance == 0:
        st.warning("⚠️ Please enter valid inputs")
    else:
        result = model.predict([[hours, attendance]])
        st.success(f"🎯 Predicted Marks: {result[0]:.2f}")

# -----------------------------
# Graph Section
# -----------------------------
st.markdown("---")
st.subheader("📈 Visualize Performance")

if st.button("📊 Show Graph"):
    hours_list = list(range(0, 13))
    predictions = [model.predict([[h, attendance]])[0] for h in hours_list]

    fig, ax = plt.subplots()
    ax.plot(hours_list, predictions, marker='o')
    ax.set_xlabel("Study Hours")
    ax.set_ylabel("Predicted Marks")
    ax.set_title("Marks vs Study Hours")

    st.pyplot(fig)

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.caption("Built by Priyansh 🚀")
