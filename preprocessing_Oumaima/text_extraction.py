from pdfminer.high_level import extract_text
import os

def extract_text_general(file_path):
    """
    Extract text from PDF, TXT, or DOCX files.
    """
    ext = os.path.splitext(file_path)[1].lower()

    try:
        # PDF
        if ext == ".pdf":
            return extract_text(file_path)

        # TXT
        elif ext == ".txt":
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                return f.read()

        # DOCX
        elif ext == ".docx":
            try:
                from docx import Document
            except ImportError:
                return ""
            doc = Document(file_path)
            return "\n".join([p.text for p in doc.paragraphs])

        else:
            return ""

    except Exception as e:
        print(f"Erreur dans extract_text_general({file_path}) : {e}")
        return ""


