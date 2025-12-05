# Streamlit application for CV Classification.
# Responsibility: Houssam

import streamlit as st
import pickle
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from preprocessing_Oumaima.text_extraction import extract_text_general
from preprocessing_Oumaima.text_cleaning import clean_text

def search_keywords(text, keywords):
    """Search for keywords in text and return matches"""
    text_lower = text.lower()
    found = []
    not_found = []
    for keyword in keywords:
        if keyword.lower().strip() in text_lower:
            found.append(keyword.strip())
        else:
            not_found.append(keyword.strip())
    return found, not_found

def main():
    st.set_page_config(page_title="CV Classification", page_icon="📄", layout="wide")
    
    st.title("📄 CV Classification System")
    st.markdown("---")
    
    # Load Model and Vectorizer
    base_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.join(base_dir, '..')
    
    model_path = os.path.join(project_root, 'modeling_MoadChafir', 'MoadChafir_model.pkl')
    vectorizer_path = os.path.join(project_root, 'modeling_MoadChafir', 'MoadChafir_vectorizer.pkl')
    
    model_loaded = False
    try:
        model = pickle.load(open(model_path, 'rb'))
        vectorizer = pickle.load(open(vectorizer_path, 'rb'))
        model_loaded = True
    except Exception as e:
        st.warning(f"Model not loaded: {e}. Classification disabled, but keyword search works.")
    
    # Create two columns
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("📤 Upload Resume")
        # Added docx support
        uploaded_file = st.file_uploader("Upload CV", type=['pdf', 'txt', 'docx'])
    
    with col2:
        st.subheader("🔍 Keyword Search")
        keywords_input = st.text_area(
            "Enter keywords (comma-separated)",
            placeholder="Python, Java, Machine Learning, SQL...",
            height=100
        )
    
    st.markdown("---")
    
    if uploaded_file is not None:
        # Save temp file
        temp_filename = "temp_cv" + os.path.splitext(uploaded_file.name)[1]
        
        with open(temp_filename, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        try:
            # Extract text
            text = extract_text_general(temp_filename)
            
            if text:
                cleaned_text = clean_text(text)
                
                # Create result columns
                result_col1, result_col2 = st.columns(2)
                
                with result_col1:
                    st.subheader("🎯 Classification Result")
                    if model_loaded:
                        if st.button("Classify CV", type="primary"):
                            features = vectorizer.transform([cleaned_text])
                            prediction = model.predict(features)[0]
                            st.success(f"**Predicted Category:** {prediction}")
                    else:
                        st.info("Model not available for classification")
                
                with result_col2:
                    st.subheader("🔎 Keyword Search Results")
                    if keywords_input:
                        keywords = [k.strip() for k in keywords_input.split(',') if k.strip()]
                        if keywords:
                            found, not_found = search_keywords(text, keywords)
                            
                            if found:
                                st.success(f"**Found ({len(found)}):** {', '.join(found)}")
                            if not_found:
                                st.error(f"**Not Found ({len(not_found)}):** {', '.join(not_found)}")
                            
                            # Show match percentage
                            match_pct = len(found) / len(keywords) * 100
                            st.metric("Match Rate", f"{match_pct:.0f}%")
                    else:
                        st.info("Enter keywords above to search")
                
                # Show extracted text in expander
                with st.expander("📝 View Extracted Text"):
                    st.text_area("Raw Text", text, height=300, disabled=True)
                
                with st.expander("🧹 View Cleaned Text"):
                    st.text_area("Cleaned Text", cleaned_text, height=200, disabled=True)
                    
            else:
                st.warning("Could not extract text from the file")
            
        except Exception as e:
            st.error(f"Error processing file: {e}")
        
        finally:
            if os.path.exists(temp_filename):
                os.remove(temp_filename)

if __name__ == "__main__":
    main()
