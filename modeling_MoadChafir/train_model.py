from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import pickle
from feature_extraction import vectorize_train

df = pd.read_csv("../data_Oumaima/processed_resumes.csv")
X = df["cleaned_text"]
y = df["category"]
x_vector = vectorize_train(X)
X_train, X_test, y_train, y_test = train_test_split(
    x_vector, y, test_size=0.2, random_state=42
)
model = RandomForestClassifier(n_estimators=100, max_depth=None, random_state=42)
model.fit(X_train, y_train)
with open("MoadChafir_model.pkl", "wb") as f:
    pickle.dump(model, f)
print("Training Complete")
def get_test_data():
    return X_test, y_test