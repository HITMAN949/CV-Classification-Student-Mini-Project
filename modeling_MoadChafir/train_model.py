# Script d'entraînement du modèle de classification de CV
# Responsable : Moad Chafir
# Ce script charge les données, entraîne un modèle Random Forest et le sauvegarde

# On importe train_test_split pour diviser nos données en ensembles d'entraînement et de test
from sklearn.model_selection import train_test_split
# RandomForestClassifier est notre algorithme de classification
from sklearn.ensemble import RandomForestClassifier
# Pandas pour manipuler les données
import pandas as pd
# Pickle pour sauvegarder notre modèle entraîné
import pickle
# On importe notre fonction de vectorisation
from feature_extraction import vectorize_train

# On charge le fichier CSV contenant les CV traités
# Ce fichier a été créé par le script process_data.py
df = pd.read_csv("../data_Oumaima/processed_resumes.csv")

# On extrait la colonne des textes nettoyés
# C'est notre variable X (les features)
X = df["cleaned_text"]

# On extrait la colonne des catégories
# C'est notre variable y (ce qu'on veut prédire)
y = df["category"]

# On transforme les textes en vecteurs numériques
# Le modèle ne comprend pas le texte brut, il lui faut des nombres
x_vector = vectorize_train(X)

# On divise nos données en ensemble d'entraînement (80%) et de test (20%)
# random_state=42 assure que la division est reproductible
X_train, X_test, y_train, y_test = train_test_split(
    x_vector, y, test_size=0.2, random_state=42
)

# On crée notre modèle Random Forest
# n_estimators=100 signifie qu'on utilise 100 arbres de décision
# max_depth=None permet aux arbres de grandir autant que nécessaire
model = RandomForestClassifier(n_estimators=100, max_depth=None, random_state=42)

# On entraîne le modèle sur nos données d'entraînement
# C'est ici que la magie opère !
model.fit(X_train, y_train)

# On sauvegarde le modèle entraîné dans un fichier pickle
# Comme ça on peut le réutiliser sans réentraîner
with open("MoadChafir_model.pkl", "wb") as f:
    pickle.dump(model, f)

# Message de confirmation
print("Training Complete")


def get_test_data():
    """
    Fonction utilitaire pour récupérer les données de test
    Utilisée par le script d'évaluation
    
    Retourne:
        X_test: Les vecteurs de test
        y_test: Les vraies catégories
    """
    return X_test, y_test