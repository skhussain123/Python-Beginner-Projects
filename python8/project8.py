import streamlit as st
import pandas as pd


st.title("Simple Data Dashboard")

height = st.slider('Enter Your Height (in cm) ', 100, 250, 175)
weight = st.slider('Enter Your Height (in cm) ', 40, 200, 70)


bmi = weight / ((height/100)**2)

st.write(f"Your Bmi {bmi:.2f}")

st.write("### BMI Category ###")
st.write("-- UnderWeight: BMI less then 18.5 --")
st.write("-- Normal Weight: BMI between 18.5 and 29.9 --")
st.write("-- over Weight: BMI between 25 and 29.9 --")

st.write("-- Obesity: BMI 30 greater --")

