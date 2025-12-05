# 📄 Automatic CV Classification

## Description
This project classifies CVs/resumes into different job categories (IT, Engineering, Marketing, etc.) using Machine Learning. It features a web interface for uploading resumes and getting instant classification results with keyword search functionality.

## 🏗️ Project Structure
```
CV Classification/
├── data_Oumaima/              # Data storage and processing
│   ├── process_data.py        # Resume processing script
│   ├── processed_resumes.csv  # Generated training data
│   └── resumes_raw/           # Raw resume files by category
│       ├── Engineering/
│       ├── Marketing/
│       └── IT/
├── preprocessing_Oumaima/     # Text preprocessing
│   ├── text_extraction.py     # Extract text from PDF/TXT/DOCX
│   └── text_cleaning.py       # Clean and normalize text
├── modeling_MoadChafir/       # ML Model
│   ├── feature_extraction.py  # TF-IDF vectorization
│   ├── train_model.py         # Model training
│   ├── evaluate.py            # Model evaluation
│   ├── MoadChafir_model.pkl   # Trained model
│   └── MoadChafir_vectorizer.pkl  # Trained vectorizer
└── interface_Houssam/         # Web Interface
    └── app.py                 # Streamlit application
```

## ⚙️ Installation

1. **Clone the repository**

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   pip install python-docx
   ```

## 🚀 Usage

### Step 1: Prepare Training Data
Place your resume files in categorized folders inside `data_Oumaima/resumes_raw/`:
```
resumes_raw/
├── Engineering/
│   ├── resume1.pdf
│   └── resume2.txt
├── IT/
│   └── it_resume.docx
└── Marketing/
    └── marketing_cv.pdf
```

### Step 2: Process Data
Run from the `data_Oumaima` directory:
```bash
cd data_Oumaima
python process_data.py
```

### Step 3: Train Model
Run from the `modeling_MoadChafir` directory:
```bash
cd modeling_MoadChafir
python train_model.py
```

### Step 4: Evaluate Model (Optional)
```bash
cd modeling_MoadChafir
python evaluate.py
```

### Step 5: Run Web Interface
```bash
streamlit run interface_Houssam/app.py
```
Then open `http://localhost:8501` in your browser.

## 🌐 Web Interface Features

### Resume Classification
- Upload resumes in **PDF**, **TXT**, or **DOCX** format
- Get instant category predictions (IT, Engineering, Marketing, etc.)

### Keyword Search
- Enter comma-separated keywords
- See which keywords are **found** ✅ or **not found** ❌
- View match rate percentage

### Text Viewer
- View extracted raw text from uploaded resume
- View cleaned/processed text

## 📁 Supported File Formats
| Format | Extension | Support |
|--------|-----------|---------|
| PDF    | `.pdf`    | ✅       |
| Text   | `.txt`    | ✅       |
| Word   | `.docx`   | ✅       |

## 🔧 Technical Details

### Model
- **Algorithm:** Random Forest Classifier
- **Features:** TF-IDF vectors (max 1000 features)
- **Train/Test Split:** 80/20

### Text Processing
- Text extraction from multiple file formats
- Lowercase conversion
- URL and email removal
- Special character removal
- Whitespace normalization

## 👥 Team
- **Oumaima** - Data & Preprocessing
- **Moad Chafir** - Model Training & Evaluation
- **Houssam** - Web Interface & Debugging & Documentation

## 📊 Predict All CVs
A new script `predict_all.py` prédit la catégorie de chaque CV présent dans `processed_resumes.csv` et enregistre le résultat dans `predicted_resumes.csv`.

```bash
python modeling_MoadChafir/predict_all.py
```

Le CSV de sortie contient une colonne supplémentaire `predicted_category` avec la prédiction du modèle pour chaque CV.


## 📝 License
This project is for educational purposes.
