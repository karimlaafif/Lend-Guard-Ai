# src/data_prep.py
import pandas as pd
from sklearn.model_selection import train_test_split

def load_data(filepath):
    """Load CSV data from Kaggle or PaySim simulator."""
    return pd.read_csv(filepath)

def clean_data(df):
    """Basic cleanup - handle missing values & encode categorical columns."""
    df.fillna(0, inplace=True)
    for col in df.select_dtypes('object'):
        df[col] = df[col].astype('category').cat.codes
    return df

def split_data(df, target):
    """Split for supervised tasks."""
    X = df.drop(columns=[target])
    y = df[target]
    return train_test_split(X, y, test_size=0.2, random_state=42)
