# Module de nettoyage de texte pour les CV
# Responsable : Oumaima
# Ce module nettoie le texte extrait pour le préparer à l'analyse

# On importe regex pour les expressions régulières
# C'est une version améliorée du module re standard
import regex


def clean_text(text):
    """
    Fonction de nettoyage de texte
    Elle supprime les URLs, emails, caractères spéciaux, etc.
    
    Arguments:
        text: Le texte brut à nettoyer
    
    Retourne:
        Le texte nettoyé, ou None si le texte d'entrée est vide
    """
    # Si le texte est vide ou None, on retourne None
    if not text:
        return  # On retourne None pour les entrées vides
    
    # Étape 1 : Conversion en minuscules
    # Cela rend la comparaison plus facile plus tard
    text = text.lower()
    
    # Étape 2 : Suppression des URLs
    # On cherche les patterns comme "http://..." ou "www...."
    text = regex.sub(r"https?://[^\s]+|www\.[^\s]+", " ", text)
    
    # Étape 3 : Suppression des adresses email
    # Le pattern détecte les formats comme "nom@domaine.com"
    text = regex.sub(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b", " ", text)
    
    # Étape 4 : Suppression des caractères spéciaux
    # On garde seulement les lettres, chiffres et espaces
    # Le flag UNICODE permet de garder les caractères accentués
    text = regex.sub(r"[^\w\s]", " ", text, flags=regex.UNICODE)
    
    # Étape 5 : Normalisation des espaces
    # On remplace les espaces multiples par un seul espace
    text = regex.sub(r"\s+", " ", text)
    
    # Étape 6 : Suppression des espaces en début et fin
    # strip() enlève les espaces superflus
    return text.strip()
