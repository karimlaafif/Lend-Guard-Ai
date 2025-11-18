# dashboard/app.py
import streamlit as st
import requests

st.title("FinRisk360+ Real-time Scoring Dashboard")

user_input = st.text_input("Transaction Data (JSON)")

if st.button("Get Credit Risk"):
    response = requests.post("http://localhost:8000/risk", json=user_input)
    st.write(response.json())

if st.button("Detect Fraud"):
    response = requests.post("http://localhost:8000/fraud", json=user_input)
    st.write(response.json())
