import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import joblib
import os

def train_model(input_path: str, model_path: str):
    df = pd.read_csv(input_path)

    # Define features and label
    X = df.drop(columns=["has_physical_copy", "patient_id"])
    y = df["has_physical_copy"]

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train Logistic Regression
    clf = LogisticRegression(max_iter=1000)
    clf.fit(X_train, y_train)

    # Evaluate
    y_pred = clf.predict(X_test)
    print("📊 Classification Report:")
    print(classification_report(y_test, y_pred))

    # Save model
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    joblib.dump(clf, model_path)
    print(f"✅ Model saved to {model_path}")

if __name__ == "__main__":
    train_model("data/claims_features.csv", "models/has_copy_model.pkl")
