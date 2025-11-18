# src/fraud_model.py
from sklearn.ensemble import IsolationForest

def train_isolation_forest(X_train):
    """Train unsupervised IsolationForest on transaction data."""
    model = IsolationForest(n_estimators=100, contamination=0.02)
    model.fit(X_train)
    return model

def detect_fraud(model, X):
    """Scores each transaction for anomaly."""
    return model.predict(X)
