import getopt
import sys
import pandas as pd

# from src.utilities.wordcloud import generate_wordcloud
from src.functions.get_tweets import recopilation_tweets
from src.methods.tokenization import tokenization
from src.utilities.parameter_editor import parameter_updater
from src.methods.stop_words import  stop_words
from src.methods.pos import labeling
from src.methods.lemmatization import lemmatization
from src.methods.lemmatization import stemming


def option_reading():
    (opt, arg) = getopt.getopt(sys.argv[1:], 'w:p:', ['word=', 'pages='])

    for (op, arg) in opt:
        if op in ['-w', '--word']:
            word = arg
        elif op in ['-p', '--pages']:
            pages = int(arg)
        else:
            print('error')
            sys.exit(0)

    assert (word, pages) is not None
    return word, pages


def main():
    word, pages = option_reading()
    parameter_updater(word)

    total_message = recopilation_tweets(pages, word)
    df = pd.json_normalize(total_message)

    tokenized_text_dataframe = tokenization(df)
    words = tokenized_text_dataframe['tokenized_text']
    #final_stop = stop_words(words)
    #pos = labeling(words)
    deviration = stemming(words)
    lematization = lemmatization(words)
    print(deviration, lematization)

    
    
    # generate_wordcloud(tokenized_text_dataframe)


if __name__ == '__main__':
    main()
