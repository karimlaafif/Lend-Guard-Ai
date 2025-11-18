# src/risk_model.py
import xgboost as xgb

def train_xgb(X_train, y_train):
    """Train XGBoost Credit Risk model."""
    model = xgb.XGBClassifier()
    model.fit(X_train, y_train)
    return model

def predict(model, X):
    """Return prediction probabilities."""
    return model.predict_proba(X)
