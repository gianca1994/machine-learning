from nltk.tokenize import TweetTokenizer


def tokenization(dataframe):
    tt = TweetTokenizer()
    tokenized_text = dataframe['text'].apply(tt.tokenize)
    dataframe["tokenized_text"] = tokenized_text
    return dataframe
