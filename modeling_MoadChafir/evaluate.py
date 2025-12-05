import pickle
from train_model import get_test_data
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

#Load data
X_test_vectors, y_test = get_test_data()
with open("MoadChafir_model.pkl", "rb") as f:
    model = pickle.load(f)
#Predict
y_pred = model.predict(X_test_vectors)
#Evaluate
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))