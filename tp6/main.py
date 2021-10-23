import pandas as pd
from src.functions.get_tweets import recopilation_tweets
from src.methods.tokenization import tokenization
from src.utilities.wordcloud import generate_wordcloud


def main():
    total_message = recopilation_tweets(5)
    df = pd.json_normalize(total_message)
    
    tokenized_text_dataframe = tokenization(df)
    generate_wordcloud(tokenized_text_dataframe)

main()

