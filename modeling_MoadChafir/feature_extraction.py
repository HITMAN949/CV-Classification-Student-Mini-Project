# Functions to convert text to TF-IDF vectors.
# Responsibility: MoadChafir

import pickle
import os
from sklearn.feature_extraction.text import TfidfVectorizer

def vectorize_train(text_series):
    # Initialize TF-IDF Vectorizer
    word_vectorizer = TfidfVectorizer(sublinear_tf=True, stop_words='english')

    # Fit and transform
    word_vectorizer.fit(text_series)
    WordFeatures = word_vectorizer.transform(text_series)

    # Save vectorizer
    if not os.path.exists('modeling_MoadChafir'):
        os.makedirs('modeling_MoadChafir')
        
    with open('modeling_MoadChafir/vectorizer.pkl', 'wb') as f:
        pickle.dump(word_vectorizer, f)

    return WordFeatures
