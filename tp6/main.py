import getopt
import sys
import os
from nltk.util import pr
import pandas as pd
from src.methods.polarity import polarity

from src.utilities.wordcloud import generate_wordcloud
from src.functions.get_tweets import recopilation_tweets
from src.methods.tokenization import tokenization
from src.utilities.parameter_editor import parameter_updater
from src.methods.stop_words import stop_words
from src.methods.pos import labeling
from src.methods.lemmatization import lemmatization
from src.methods.lemmatization import stemming

from src.utilities.cleaner import cleaner

def option_reading():
    (opt, arg) = getopt.getopt(sys.argv[1:], 'w:p:l:', ['word=', 'pages=', 'lang='])

    for (op, arg) in opt:
        if op in ['-w', '--word']:
            word = arg
        elif op in ['-p', '--pages']:
            pages = int(arg)
        elif op in ['-l', '--lang']:
            lang = arg
        else:
            print('error')
            sys.exit(0)

    assert (word, pages, lang) is not None
    return word, pages, lang


def main():

    word, pages, lang = option_reading()
    

    if not os.path.isdir('results'):
        os.mkdir('results')

    if not os.path.isdir(f'results/{word}'):
        os.mkdir(f'results/{word}')

    parameter_updater(word, lang)

    total_message = recopilation_tweets(pages, word, lang)

    df = pd.json_normalize(total_message)
    df_new = cleaner(df)

    tokenized_text_dataframe = tokenization(df_new)
    words = tokenized_text_dataframe['tokenized_text']

    # Stop Words
    tokens_without_sw = stop_words(words, word, lang)

    # Etiquetado POS
    labeling(words, word)

    # Derivacion
    stemming(words, word)

    # Lematizacion
    lemmatization(words, word)

    generate_wordcloud(tokens_without_sw, word)


if __name__ == '__main__':
    main()
