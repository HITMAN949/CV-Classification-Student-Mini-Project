# Script de traitement des données de CV
# Responsable : Oumaima
# Ce script parcourt les CV bruts et crée un fichier CSV pour l'entraînement

# On importe os pour manipuler les fichiers et dossiers
import os
# Pandas nous permet de créer et manipuler des tableaux de données
import pandas as pd

# On importe notre fonction d'extraction de texte
# Elle gère les fichiers PDF, TXT et DOCX
from preprocessing_Oumaima.text_extraction import extract_text_general
# On importe la fonction de nettoyage de texte
from preprocessing_Oumaima.text_cleaning import clean_text


def process_resumes(base_dir="resumes_raw"):
    """
    Fonction principale pour traiter tous les CV
    Elle parcourt les dossiers de catégories et extrait le texte de chaque CV
    """
    # Liste pour stocker toutes les données extraites
    all_data = []
    # Extensions de fichiers qu'on sait traiter
    valid_extensions = [".pdf", ".txt", ".docx"]

    # On parcourt chaque dossier dans le répertoire de base
    # Chaque dossier représente une catégorie (IT, Marketing, etc.)
    for category in os.listdir(base_dir):
        # On construit le chemin complet vers le dossier de catégorie
        category_path = os.path.join(base_dir, category)

        # On vérifie que c'est bien un dossier (pas un fichier)
        if os.path.isdir(category_path):
            # On parcourt chaque fichier dans ce dossier de catégorie
            for filename in os.listdir(category_path):
                # Chemin complet vers le fichier
                file_path = os.path.join(category_path, filename)

                # On vérifie si l'extension du fichier est supportée
                if not any(filename.lower().endswith(ext) for ext in valid_extensions):
                    # Si l'extension n'est pas supportée, on affiche un message et on passe au suivant
                    print(f"Fichier ignoré (extension non supportée) : {filename}")
                    continue

                # On essaie d'extraire le texte du fichier
                text = extract_text_general(file_path)
                # Si l'extraction a échoué (texte vide)
                if not text:
                    print(f"Impossible d'extraire le texte depuis : {filename}")
                    continue

                # On nettoie le texte extrait
                # Cela enlève les caractères spéciaux, met en minuscules, etc.
                cleaned_text = clean_text(text)

                # On ajoute les données à notre liste
                # Chaque entrée contient la catégorie, le nom du fichier, et les deux versions du texte
                all_data.append({
                    "category": category,
                    "filename": filename,
                    "raw_text": text,
                    "cleaned_text": cleaned_text
                })

    # On convertit notre liste en DataFrame pandas
    # C'est plus pratique pour sauvegarder en CSV
    df = pd.DataFrame(all_data)
    # Chemin du fichier CSV de sortie
    output_csv = "processed_resumes.csv"
    # On sauvegarde le DataFrame en CSV
    # index=False pour ne pas avoir de colonne d'index
    # encoding="utf-8" pour supporter les caractères spéciaux
    df.to_csv(output_csv, index=False, encoding="utf-8")

    # On affiche un résumé de ce qu'on a fait
    print(f"\nCSV créé avec succès : {output_csv}")
    print(f"Nombre de CV traités : {len(df)}")


# Point d'entrée du script
# Ce bloc s'exécute seulement si on lance ce fichier directement
if __name__ == "__main__":
    # On lance le traitement des CV
    process_resumes()
