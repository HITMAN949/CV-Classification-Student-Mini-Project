import re
import string
import spacy
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
import warnings
warnings.filterwarnings('ignore')

try:
    nlp = spacy.load('en_core_web_sm')
except OSError:
    print("Downloading 'en_core_web_sm' model...")
    from spacy.cli import download
    download("en_core_web_sm")
    nlp = spacy.load('en_core_web_sm')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')
my_stop_words = set(stopwords.words('english') + ['``', "''"])
def remove_pattern(text, pattern_regex):
    """
    Removes a specific regex pattern from the text.
    """
    r = re.findall(pattern_regex, text)
    for i in r:
        text = re.sub(i, '', text)
    return text
def remove_emoji(text):
    """
    Removes emojis from the text.
    """
    emoji_pattern = re.compile(
        u"[\U0001F600-\U0001F64F"  
        u"\U0001F300-\U0001F5FF"  
        u"\U0001F680-\U0001F6FF"  
        u"\U0001F1E0-\U0001F1FF"
        u"\u24C2\u1F150-\u1F151"
        u"]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)
def clean_text(text):
    """
    Performs basic text cleaning: lowercasing, removing URLs, punctuation, numbers, etc.
    """
    text = text.lower()
    text = re.sub('!', '', text)
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('⇨', '', text)
    text = re.sub(':', '', text)
    text = re.sub('•', '', text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    return text
def preprocess_pipeline(text):
    """
    Complete preprocessing pipeline:
    1. Clean text (remove noise)
    2. Remove emojis
    3. Remove stop words
    4. Lemmatize
    """
    
    text = clean_text(text)

    text = remove_emoji(text)
    
    
    tokens = text.split()
    tokens = [word for word in tokens if word not in my_stop_words]
    
    
    text = " ".join(tokens)
    
    
    doc = nlp(text)
    lemmas = [token.lemma_ for token in doc]
    
   
    return " ".join(lemmas)

cv_ngram_range = CountVectorizer(analyzer='word', ngram_range=(1,3), max_features=4000)
if __name__ == "__main__":
    
    sample_text = "Experienced Software Engineer with skills in Python, Java, and 10+ years of experience! 🚀"
    processed_text = preprocess_pipeline(sample_text)
    print(f"Original: {sample_text}")
    print(f"Processed: {processed_text}")
    
    
    corpus = [processed_text]
    matrix = cv_ngram_range.fit_transform(corpus)
    print(f"Vectorized shape: {matrix.shape}")