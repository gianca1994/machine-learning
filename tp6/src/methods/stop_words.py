from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def stop_words(words, word, lang):
    final = []

    for i in words:
        for j in i:
            final.append(j)

    all_words = " ".join(map(str.lower, final))

    all_stop = stopwords.words('spanish') if lang == 'es' else stopwords.words('english')
    print(all_stop)
    text_tokens = word_tokenize(all_words)
    tokens_without_sw = []

    for i in text_tokens:
        if not i in all_stop:
            tokens_without_sw.append(i)

    file = open (f'results/{word}/{word}-StopWords.csv', 'w')
    for i in tokens_without_sw:    
        file.write(i + "\n")
    file.close()

    return tokens_without_sw


