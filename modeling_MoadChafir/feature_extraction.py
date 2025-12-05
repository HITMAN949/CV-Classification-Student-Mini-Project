# Module d'extraction de caractéristiques (features)
# Responsable : Moad Chafir
# Ce module transforme le texte en vecteurs numériques avec TF-IDF

# TfidfVectorizer transforme le texte en vecteurs TF-IDF
# TF-IDF = Term Frequency - Inverse Document Frequency
# C'est une technique qui donne plus d'importance aux mots rares et distinctifs
from sklearn.feature_extraction.text import TfidfVectorizer
# Pickle pour sauvegarder notre vectoriseur
import pickle


def vectorize_train(text_series):
    """
    Fonction pour vectoriser les textes d'entraînement
    Elle crée un vectoriseur TF-IDF, l'entraîne et le sauvegarde
    
    Arguments:
        text_series: Une série pandas contenant les textes à vectoriser
    
    Retourne:
        Une matrice sparse contenant les vecteurs TF-IDF
    """
    # On crée le vectoriseur TF-IDF
    # max_features=1000 limite le vocabulaire aux 1000 mots les plus importants
    # Cela évite d'avoir un modèle trop gros
    vectorizer = TfidfVectorizer(max_features=1000)
    
    # On entraîne le vectoriseur et on transforme les textes en une seule étape
    # fit_transform() fait les deux opérations à la fois
    x = vectorizer.fit_transform(text_series)
    
    # On sauvegarde le vectoriseur pour pouvoir l'utiliser plus tard
    # On en aura besoin pour transformer les nouveaux CV à classifier
    with open("MoadChafir_vectorizer.pkl", "wb") as f:
        pickle.dump(vectorizer, f)
    
    # On retourne la matrice de vecteurs
    return x