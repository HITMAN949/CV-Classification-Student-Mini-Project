# Automatic CV Classification

## Description
This project aims to classify CVs into different domains (IT, Marketing, Finance, etc.) using Machine Learning.

## Structure
- `data_Oumaima/`: Data storage and generation.
- `preprocessing_Oumaima/`: Text extraction and cleaning.
- `modeling_MoadChafir/`: Model training and evaluation.
- `interface_Houssam/`: Streamlit web interface.
- `reports_All/`: Project documentation.
- `tests_All/`: Unit tests.

## Installation
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   python -m spacy download en_core_web_sm
   ```

## Usage
1. Prepare Data:
   Place your PDF/TXT resumes in categorized folders inside `data_Oumaima/resumes_raw/`.
   Example: `data_Oumaima/resumes_raw/IT/resume1.pdf`

2. Process Data:
   ```bash
   python data_Oumaima/process_data.py
   ```

3. Train Model:
   ```bash
   python modeling_MoadChafir/train_model.py
   ```

4. Run the app:
   ```bash
   streamlit run interface_Houssam/app.py
   ```
