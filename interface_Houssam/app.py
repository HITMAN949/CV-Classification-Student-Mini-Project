# Streamlit application for CV Classification.
# Responsibility: Houssam

import streamlit as st
import pickle
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from preprocessing_Oumaima.text_extraction import extract_text_from_file
from preprocessing_Oumaima.text_cleaning import clean_text

def main():
    st.title("CV Classification System")
    
    # Load Model and Vectorizer
    base_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.join(base_dir, '..')
    
    model_path = os.path.join(project_root, 'modeling_MoadChafir', 'model.pkl')
    vectorizer_path = os.path.join(project_root, 'modeling_MoadChafir', 'vectorizer.pkl')
    
    try:
        model = pickle.load(open(model_path, 'rb'))
        vectorizer = pickle.load(open(vectorizer_path, 'rb'))
    except:
        st.error("Error loading model")
        return

    uploaded_file = st.file_uploader("Upload CV", type=['pdf', 'txt'])
    
    if st.button("Classify"):
        if uploaded_file is not None:
            # Save temp file
            temp_filename = "temp_cv" + os.path.splitext(uploaded_file.name)[1]
            
            with open(temp_filename, "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            try:
                text = extract_text_from_file(temp_filename)
                
                if text:
                    cleaned_text = clean_text(text)
                    features = vectorizer.transform([cleaned_text])
                    prediction = model.predict(features)[0]
                    st.success(f"Predicted Category: {prediction}")
                else:
                    st.warning("Could not extract text")
                
            except Exception as e:
                st.error(f"Error: {e}")
            
            if os.path.exists(temp_filename):
                os.remove(temp_filename)
        else:
            st.warning("Please upload a file.")

if __name__ == "__main__":
    main()
