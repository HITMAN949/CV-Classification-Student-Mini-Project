import pickle
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split

# --- Load test data ---
df = pd.read_csv("data_Oumaima/processed_resumes.csv")
X = df["text"]
y = df["category"]
# Split data
_, X_test_raw, _, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
with open("MoadChafir_model.pkl", "rb") as f:
    model = pickle.load(f)
with open("MoadChafir_vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)
X_test_vectors = vectorizer.transform(X_test_raw)
# --- Predict ---
y_pred = model.predict(X_test_vectors)
# --- Evaluate ---
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))