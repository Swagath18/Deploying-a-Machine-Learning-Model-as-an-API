import pandas as pd
import numpy as np
import os

def clean_claims_data(input_path: str, output_path: str):
    df = pd.read_csv(input_path)

    # 1. Impute missing age with median
    df["age"] = df["age"].fillna(df["age"].median())

    # 2. Impute missing claim_amount with median
    df["claim_amount"] = df["claim_amount"].fillna(df["claim_amount"].median())

    # 3. Impute diagnosis_code with mode
    df["diagnosis_code"] = df["diagnosis_code"].fillna(df["diagnosis_code"].mode()[0])

    # 4. Normalize data types
    df["claim_date"] = pd.to_datetime(df["claim_date"])
    df["has_physical_copy"] = df["has_physical_copy"].astype(bool)

    # 5. Outlier handling (e.g., clamp claim_amount to 1st-99th percentile)
    lower = df["claim_amount"].quantile(0.01)
    upper = df["claim_amount"].quantile(0.99)
    df["claim_amount"] = df["claim_amount"].clip(lower, upper)

    # 6. Feature sanity check
    assert not df.isnull().any().any(), "There are still missing values!"

    # Save cleaned version
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"✅ Cleaned data saved to {output_path}")

if __name__ == "__main__":
    clean_claims_data("data/claims_deidentified.csv", "data/claims_cleaned.csv")
