# 📄 Projet : Classification Automatique des CV

**Équipe** :
- **Brahimi Oumaima**
- **Chafir Moad**
- **Lasfar Houssam**

**Professeur** : M. Meddaoui

---

## 🎯 Contexte du projet
Le professeur Meddaoui nous a demandé de développer un système capable de **lire des CV** (au format texte ou PDF) et de les **classer automatiquement** selon le domaine professionnel (informatique, marketing, finance, etc.) ou le niveau d'expérience.

## 📚 Objectifs pédagogiques
- **Extraction du texte brut** des CV.
- **Représentation vectorielle** des CV (TF‑IDF).
- **Entraînement d’un modèle de classification** supervisée.

## ✅ Fonctionnalités minimales implémentées
- Nettoyage et **tokenisation** du texte (suppression des URLs, e‑mails, caractères spéciaux, normalisation des espaces, mise en minuscules).
- Utilisation de **TF‑IDF** pour transformer les CV en vecteurs numériques.
- Classification **supervisée** avec un **Random Forest** (vous pouvez facilement remplacer par SVM ou régression logistique).
- **Interface Streamlit** simple permettant de déposer un CV (PDF, TXT ou DOCX) et d’obtenir la catégorie prédite.
- Recherche de **mots‑clés** dans le CV avec affichage du taux de correspondance.

## 🌟 Fonctionnalités avancées (bonus)
- Extraction de **compétences clés** via recherche de mots‑clés fournis par l’utilisateur.
- Affichage du **texte brut** et du **texte nettoyé** pour vérification.
- Possibilité d’ajouter un **matching** CV ↔ poste en fonction des mots‑clés.

## 🛠️ Technologies / Bibliothèques utilisées
- **Python 3.x**
- `pandas`, `numpy`, `scikit‑learn`
- `pdfminer.six` pour l’extraction de texte PDF
- `python‑docx` pour les fichiers DOCX
- `streamlit` pour l’interface web

## 📂 Structure du projet
```
CV Classification/
├── data_Oumaima/                # Données brutes et CSV traité
│   ├── resumes_raw/            # CVs classés par catégorie (IT, Marketing, …)
│   └── processed_resumes.csv   # CSV généré pour l’entraînement
├── preprocessing_Oumaima/       # Extraction et nettoyage du texte
│   ├── text_extraction.py
│   └── text_cleaning.py
├── modeling_MoadChafir/         # Modélisation
│   ├── feature_extraction.py   # TF‑IDF + sauvegarde du vectoriseur
│   ├── train_model.py          # Entraînement du modèle
│   ├── evaluate.py             # Évaluation du modèle
│   ├── MoadChafir_model.pkl    # Modèle entraîné
│   └── MoadChafir_vectorizer.pkl
└── interface_Houssam/           # Application Streamlit
    └── app.py
```

## 📦 Livrables attendus
1. **Code complet** (déposé dans le dépôt Git).
2. **Jeu de CV fictifs** (au moins 5 CV par catégorie).
3. **Rapport explicatif** décrivant :
   - Le processus d’extraction et de nettoyage.
   - Le choix du modèle et les hyper‑paramètres.
   - Les métriques de performance (accuracy, classification report, matrice de confusion).
   - Les limites du système et les pistes d’amélioration.

---

## 🚀 Comment lancer le projet
```bash
# 1. Installer les dépendances
pip install -r requirements.txt
pip install python-docx

# 2. Traiter les CV bruts
python data_Oumaima/process_data.py

# 3. Entraîner le modèle
python modeling_MoadChafir/train_model.py

# 4. (Optionnel) Évaluer le modèle
python modeling_MoadChafir/evaluate.py

# 5. Lancer l’interface web
streamlit run interface_Houssam/app.py
```

Vous pouvez maintenant déposer un CV et obtenir instantanément sa catégorie ainsi que la présence des mots‑clés que vous avez spécifiés.

---

*Ce projet a été réalisé dans le cadre du cours de **Programmation Python** sous la supervision du Professeur Meddaoui.*
