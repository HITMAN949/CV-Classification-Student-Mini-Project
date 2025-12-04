import os
import pandas as pd
import sys

# Add project root to path to import preprocessing modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from preprocessing_Oumaima.text_extraction import extract_text_from_file
from preprocessing_Oumaima.text_cleaning import clean_text

def process_resumes(raw_data_dir, output_csv_path):
    """
    Reads CVs from subdirectories in raw_data_dir, extracts text, cleans it,
    and saves the dataset to a CSV file.
    
    Args:
        raw_data_dir (str): Path to the directory containing categorized CVs.
                            Structure: raw_data_dir/Category/cv.pdf
        output_csv_path (str): Path to save the processed CSV.
    """
    if not os.path.exists(raw_data_dir):
        print(f"Error: Directory {raw_data_dir} does not exist.")
        return

    data = []
    
    # Iterate through each category folder
    for category in os.listdir(raw_data_dir):
        category_path = os.path.join(raw_data_dir, category)
        
        if os.path.isdir(category_path):
            print(f"Processing category: {category}")
            for filename in os.listdir(category_path):
                file_path = os.path.join(category_path, filename)
                
                if os.path.isfile(file_path):
                    # Extract text
                    text = extract_text_from_file(file_path)
                    
                    if text:
                        # Clean text
                        cleaned_text = clean_text(text)
                        
                        if cleaned_text:
                            data.append({
                                'filename': filename,
                                'text': cleaned_text,
                                'category': category
                            })
                        else:
                            print(f"Warning: Empty text after cleaning for {filename}")
                    else:
                        print(f"Warning: Could not extract text from {filename}")

    if data:
        df = pd.DataFrame(data)
        df.to_csv(output_csv_path, index=False)
        print(f"Success! Processed {len(df)} resumes. Data saved to {output_csv_path}")
    else:
        print("No data found or processed.")

if __name__ == "__main__":
    # Define paths
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    RAW_RESUMES_DIR = os.path.join(BASE_DIR, 'resumes_raw')
    OUTPUT_CSV = os.path.join(BASE_DIR, 'processed_resumes.csv')
    
    print(f"Looking for resumes in: {RAW_RESUMES_DIR}")
    process_resumes(RAW_RESUMES_DIR, OUTPUT_CSV)
