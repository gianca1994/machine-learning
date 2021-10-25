from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer

def stemming(words):
    ps = PorterStemmer()
    
    for i in words:
        for j in i:
            return ps.stem(j)

def lemmatization(words):
    wordnet_lemmatizer = WordNetLemmatizer()

    for i in words:
        for j in i:
            return wordnet_lemmatizer.lemmatize(j)

