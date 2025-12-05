import os
import pandas as pd
from preprocessing_Oumaima.text_extraction import extract_text_general
from preprocessing_Oumaima.text_cleaning import clean_text

def process_resumes(base_dir="data_Oumaima/resumes_raw"):
    all_data = []
    valid_extensions = [".pdf", ".txt", ".docx"]

    for category in os.listdir(base_dir):
        category_path = os.path.join(base_dir, category)

        if os.path.isdir(category_path):
            for filename in os.listdir(category_path):
                file_path = os.path.join(category_path, filename)

                # Vérification extension
                if not any(filename.lower().endswith(ext) for ext in valid_extensions):
                    print(f"Fichier ignoré (extension non supportée) : {filename}")
                    continue

                # Extraction texte
                text = extract_text_general(file_path)
                if not text:
                    print(f"Impossible d'extraire le texte depuis : {filename}")
                    continue

                # Nettoyage
                cleaned_text = clean_text(text)

                all_data.append({
                    "category": category,
                    "filename": filename,
                    "raw_text": text,
                    "cleaned_text": cleaned_text
                })

    df = pd.DataFrame(all_data)
    output_csv = "data_Oumaima/processed_resumes.csv"
    df.to_csv(output_csv, index=False, encoding="utf-8")

    print(f"\nCSV créé avec succès : {output_csv}")
    print(f"Nombre de CV traités : {len(df)}")

if __name__ == "__main__":
    process_resumes()
