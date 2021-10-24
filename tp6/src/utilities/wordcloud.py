"""from wordcloud import WordCloud
import matplotlib.pyplot as plt

def generate_wordcloud(dataframe):
    wordcloud = WordCloud(
        max_words=100,
        background_color="white"
    ).generate(dataframe['tokenized_text'].to_string())

    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.rcParams['figure.figsize'] = [150, 150]
    plt.show()
"""