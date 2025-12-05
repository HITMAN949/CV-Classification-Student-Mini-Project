import regex 

def clean_text(text):
    if not text:
        return #return none for empty input 
    text = text.lower()
    
    text = regex.sub(r"https?://[^\s]+|www\.[^\s]+", " ", text)
    
    text = regex.sub(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b", " ", text)
    
    text = regex.sub(r"[^\w\s]", " ", text, flags=regex.UNICODE)
   
    text = regex.sub(r"\s+", " ", text)
    
    return text.strip()
