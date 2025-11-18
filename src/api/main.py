# src/api/main.py
from fastapi import FastAPI
import pandas as pd
from src.risk_model import train_xgb, predict
from src.fraud_model import train_isolation_forest, detect_fraud

app = FastAPI()

@app.post("/risk")
def credit_risk(payload: dict):
    # Dummy logic - extend as needed
    df = pd.DataFrame([payload])
    risk_score = predict(some_model, df)
    return {"risk_score": risk_score.tolist()}

@app.post("/fraud")
def fraud_alert(payload: dict):
    df = pd.DataFrame([payload])
    anomaly_score = detect_fraud(some_fraud_model, df)
    return {"anomaly_score": anomaly_score.tolist()}
