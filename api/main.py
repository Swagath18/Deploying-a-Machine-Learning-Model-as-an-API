from fastapi import FastAPI
from api.input_schema import ClaimInput
import joblib
import pandas as pd

app = FastAPI()
model = joblib.load("models/has_copy_model.pkl")

@app.get("/")
def read_root():
    return {"message": "Healthcare Claims ML API is running."}

@app.post("/predict")
def predict_claim(input_data: ClaimInput):
    input_dict = input_data.dict()
    input_df = pd.DataFrame([input_dict])
    prediction = int(model.predict(input_df)[0])
    probability = model.predict_proba(input_df)[0][prediction]
    return {
        "prediction": prediction,
        "confidence": round(float(probability), 3)
    }

