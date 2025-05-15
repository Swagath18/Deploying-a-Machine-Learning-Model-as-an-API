import pandas as pd
import os

def engineer_features(input_path: str, output_path: str):
    df = pd.read_csv(input_path, parse_dates=["claim_date"])

    # 1. Age Bucketing
    df["age_group"] = pd.cut(
        df["age"],
        bins=[0, 25, 40, 60, 120],
        labels=["young", "adult", "middle_aged", "senior"]
    )

    # 2. Date Features
    df["claim_dayofweek"] = df["claim_date"].dt.dayofweek
    df["claim_month"] = df["claim_date"].dt.month

    # 3. Encode Gender (binary encoding)
    df["gender"] = df["gender"].map({"M": 0, "F": 1})

    # 4. One-hot encode diagnosis_code (top 5 only)
    top_codes = df["diagnosis_code"].value_counts().nlargest(5).index.tolist()
    df["diagnosis_code"] = df["diagnosis_code"].apply(lambda x: x if x in top_codes else "Other")
    df = pd.get_dummies(df, columns=["diagnosis_code", "age_group"], prefix=["diag", "age"])

    # 5. Drop unused
    df.drop(columns=["notes", "claim_date"], inplace=True)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"✅ Features engineered and saved to {output_path}")

if __name__ == "__main__":
    engineer_features("data/claims_cleaned.csv", "data/claims_features.csv")
