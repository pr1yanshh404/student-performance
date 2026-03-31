import streamlit as st
import pickle

model = pickle.load(open('model.pkl','rb'))

st.title("Student Marks Predictor")

hours = st.number_input("Study Hours")
attendance = st.number_input("Attendance")

if st.button("Predict"):
    result = model.predict([[hours, attendance]])
    st.write("Marks:", result[0])
