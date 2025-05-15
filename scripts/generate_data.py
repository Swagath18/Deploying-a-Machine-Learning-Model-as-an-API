# scripts/generate_data.py
import pandas as pd
import numpy as np
import os

def generate_synthetic_data(save_path: str, num_records: int = 10000):
    np.random.seed(42)
    data = pd.DataFrame({
        "patient_id": np.arange(1, num_records + 1),
        "age": np.random.randint(18, 90, size=num_records),
        "gender": np.random.choice(["M", "F"], size=num_records),
        "diagnosis_code": np.random.choice(["A10", "B20", "C30", "D40", "E50"], size=num_records),
        "claim_amount": np.round(np.random.normal(5000, 1500, size=num_records), 2),
        "claim_date": pd.to_datetime("2023-01-01") + pd.to_timedelta(np.random.randint(0, 365, size=num_records), unit="d"),
        "provider_id": np.random.randint(100, 200, size=num_records),
        "has_physical_copy": np.random.choice([True, False], size=num_records),
        "notes": np.random.choice([
            "Patient requires follow-up",
            "Routine check-up completed",
            "Prescribed medication",
            "Referred to specialist",
            "Lab tests required"
        ], size=num_records)
    })

    # Inject missing values
    for col in ["age", "claim_amount", "diagnosis_code"]:
        data.loc[data.sample(frac=0.05).index, col] = np.nan

    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    data.to_csv(save_path, index=False)
    print(f"✅ Data saved to {save_path}")

if __name__ == "__main__":
    generate_synthetic_data("data/synthetic_claims.csv")
