# src/feature_eng.py
def add_features(df):
    """Create features e.g., spending ratios, transaction velocity."""
    df['transaction_velocity'] = df['amount'] / (df['timestamp'] + 1)
    df['spender_ratio'] = df['amount'] / (df['income'] + 1)
    # Add more features as needed
    return df
