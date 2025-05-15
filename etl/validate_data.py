import pandas as pd

def validate_claims_data(file_path: str):
    df = pd.read_csv(file_path)

    # Schema check
    expected_columns = {
        "patient_id": int,
        "age": float,  # pandas float if median-imputed
        "gender": object,
        "diagnosis_code": object,
        "claim_amount": float,
        "claim_date": object,
        "has_physical_copy": bool,
        "notes": object
    }

    # 1. Check columns
    assert all(col in df.columns for col in expected_columns), "❌ Missing expected columns!"

    # 2. Type checks (approximate due to pandas typing)
    for col, dtype in expected_columns.items():
        if col not in df.columns:
            continue
        inferred_type = df[col].dtype
        print(f"{col} → {inferred_type}")

    # 3. Value range checks
    assert df["age"].between(0, 120).all(), "❌ Invalid ages found!"
    assert df["claim_amount"].between(0, 100000).all(), "❌ Claim amount outliers detected!"
    assert df["gender"].isin(["M", "F"]).all(), "❌ Invalid gender values!"

    # 4. Null check
    assert not df.isnull().any().any(), "❌ Null values still exist!"

    print("✅ Data validation passed.")

if __name__ == "__main__":
    validate_claims_data("data/claims_cleaned.csv")
