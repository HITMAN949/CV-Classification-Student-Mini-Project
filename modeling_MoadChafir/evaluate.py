# Script d'évaluation du modèle de classification
# Responsable : Moad Chafir
# Ce script charge le modèle entraîné et évalue ses performances

# Pickle pour charger notre modèle sauvegardé
import pickle
# On importe la fonction pour récupérer les données de test
from train_model import get_test_data
# On importe les métriques d'évaluation de scikit-learn
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# On récupère les données de test depuis le script d'entraînement
# X_test_vectors contient les CV vectorisés
# y_test contient les vraies catégories
X_test_vectors, y_test = get_test_data()

# On charge notre modèle entraîné depuis le fichier pickle
with open("MoadChafir_model.pkl", "rb") as f:
    model = pickle.load(f)

# On utilise le modèle pour prédire les catégories des CV de test
# C'est le moment de vérité !
y_pred = model.predict(X_test_vectors)

# On affiche les différentes métriques d'évaluation

# L'accuracy : pourcentage de prédictions correctes
print("Accuracy:", accuracy_score(y_test, y_pred))

# Le rapport de classification : précision, rappel et F1-score par catégorie
# C'est plus détaillé que juste l'accuracy
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# La matrice de confusion : montre les erreurs de classification
# Les lignes sont les vraies catégories, les colonnes sont les prédictions
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))