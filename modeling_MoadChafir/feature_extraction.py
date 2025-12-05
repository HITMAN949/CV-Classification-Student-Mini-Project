from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

def vectorize_train(text_series):
#Creating vectorizer and setting a limit
    vectorizer = TfidfVectorizer(max_features=1000)
#generate matrix
    x = vectorizer.fit_transform(text_series)
#pickeling
    with open("MoadChafir_vectorizer.pkl", "wb") as f:
        pickle.dump(vectorizer, f)
    return x