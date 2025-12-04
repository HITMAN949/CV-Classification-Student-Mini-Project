import os
from pdfminer.high_level import extract_text

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a PDF file using pdfminer.six.
    
    Args:
        pdf_path (str): Path to the PDF file.
        
    Returns:
        str: Extracted text.
    """
    try:
        text = extract_text(pdf_path)
        return text
    except Exception as e:
        print(f"Error extracting text from PDF {pdf_path}: {e}")
        return ""

def extract_text_from_txt(txt_path):
    """
    Extracts text from a TXT file.
    
    Args:
        txt_path (str): Path to the TXT file.
        
    Returns:
        str: Extracted text.
    """
    try:
        with open(txt_path, 'r', encoding='utf-8', errors='ignore') as f:
            text = f.read()
        return text
    except Exception as e:
        print(f"Error extracting text from TXT {txt_path}: {e}")
        return ""

def extract_text_from_file(file_path):
    """
    Dispatcher function to extract text based on file extension.
    
    Args:
        file_path (str): Path to the file.
        
    Returns:
        str: Extracted text.
    """
    if file_path.lower().endswith('.pdf'):
        return extract_text_from_pdf(file_path)
    elif file_path.lower().endswith('.txt'):
        return extract_text_from_txt(file_path)
    else:
        print(f"Unsupported file format: {file_path}")
        return ""
