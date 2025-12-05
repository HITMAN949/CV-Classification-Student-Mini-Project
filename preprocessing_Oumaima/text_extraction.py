# Module d'extraction de texte depuis différents formats de fichiers
# Responsable : Oumaima
# Ce module gère l'extraction de texte depuis PDF, TXT et DOCX

# On importe pdfminer pour extraire le texte des fichiers PDF
from pdfminer.high_level import extract_text
# OS pour vérifier les extensions de fichiers
import os


def extract_text_general(file_path):
    """
    Fonction universelle d'extraction de texte
    Elle détecte le type de fichier et utilise la bonne méthode d'extraction
    
    Arguments:
        file_path: Chemin vers le fichier à traiter
    
    Retourne:
        Le texte extrait du fichier, ou une chaîne vide en cas d'erreur
    """
    # On récupère l'extension du fichier et on la met en minuscules
    ext = os.path.splitext(file_path)[1].lower()

    # On essaie d'extraire le texte (avec gestion des erreurs)
    try:
        # Cas 1 : Fichier PDF
        if ext == ".pdf":
            # On utilise pdfminer pour extraire le texte
            return extract_text(file_path)

        # Cas 2 : Fichier texte simple
        elif ext == ".txt":
            # On ouvre le fichier en lecture
            # encoding="utf-8" pour les caractères spéciaux
            # errors="ignore" pour ignorer les caractères problématiques
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                # On lit tout le contenu
                return f.read()

        # Cas 3 : Fichier Word (DOCX)
        elif ext == ".docx":
            # On essaie d'importer python-docx
            # Il n'est peut-être pas installé sur tous les systèmes
            try:
                from docx import Document
            except ImportError:
                # Si python-docx n'est pas installé, on retourne vide
                return ""
            # On ouvre le document Word
            doc = Document(file_path)
            # On extrait le texte de chaque paragraphe et on les joint
            return "\n".join([p.text for p in doc.paragraphs])

        # Cas 4 : Extension non supportée
        else:
            # On retourne une chaîne vide
            return ""

    # En cas d'erreur quelconque
    except Exception as e:
        # On affiche l'erreur pour le débogage
        print(f"Erreur dans extract_text_general({file_path}) : {e}")
        # On retourne une chaîne vide
        return ""
