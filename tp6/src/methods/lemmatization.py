from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer


def stemming(words, word):
    ps = PorterStemmer()

    file = open (f'results/{word}/{word}-Stemming.csv', 'w')
    for i in words:
        for j in i:
            return ps.stem(j)
    file.close()


def lemmatization(words, word):
    wordnet_lemmatizer = WordNetLemmatizer()

    file = open (f'results/{word}/{word}-Lematizer.csv', 'w')
    for i in words: 
        for j in i: 
            file.write(wordnet_lemmatizer.lemmatize(j) + "\n")
    file.close()

