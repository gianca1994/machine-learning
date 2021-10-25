from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def stop_words(words):
    final = []
    for i in words:
        for j in i:
            final.append(j)
    all_words = " ".join(map(str.lower, final))
    all_stop = stopwords.words('spanish')
    all_stop.append('siguen')
    text_tokens = word_tokenize(all_words)
    tokens_without_sw = []
    

    for i in text_tokens:
        if not i in all_stop:
            tokens_without_sw.append(i)  

    return tokens_without_sw


    