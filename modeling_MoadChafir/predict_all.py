# Script pour prédire la catégorie de chaque CV présent dans le fichier CSV traité
# Responsable : Moad Chafir (extension du script existant)

import pandas as pd
import pickle
import os

# Chemins relatifs depuis ce script
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
model_path = os.path.join(project_root, 'modeling_MoadChafir', 'MoadChafir_model.pkl')
vectorizer_path = os.path.join(project_root, 'modeling_MoadChafir', 'MoadChafir_vectorizer.pkl')
processed_csv = os.path.join(project_root, 'data_Oumaima', 'processed_resumes.csv')
output_csv = os.path.join(project_root, 'data_Oumaima', 'predicted_resumes.csv')

# Chargement du modèle et du vectoriseur
with open(model_path, 'rb') as f:
    model = pickle.load(f)
with open(vectorizer_path, 'rb') as f:
    vectorizer = pickle.load(f)

# Lecture du CSV contenant les CV nettoyés
df = pd.read_csv(processed_csv)

# Vérification de la présence de la colonne "cleaned_text"
if 'cleaned_text' not in df.columns:
    raise KeyError('La colonne "cleaned_text" est manquante dans le CSV traité.')

# Transformation du texte en vecteurs TF‑IDF
X = vectorizer.transform(df['cleaned_text'])

# Prédiction des catégories
predictions = model.predict(X)

# Ajout des prédictions au DataFrame
df['predicted_category'] = predictions

# Sauvegarde du résultat dans un nouveau CSV
df.to_csv(output_csv, index=False, encoding='utf-8')

print(f"Prédictions terminées. Résultat sauvegardé dans : {output_csv}")
