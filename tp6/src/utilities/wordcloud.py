from wordcloud import WordCloud
import matplotlib.pyplot as plt


def generate_wordcloud(dataframe, word_name):

    dataframe_string = " ".join(map(str, dataframe))

    wordcloud = WordCloud(
        max_words=50,
        height=1000,
        width=1000,
        background_color="black"
    ).generate(dataframe_string)

    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.rcParams['figure.figsize'] = [150, 150]
    plt.savefig(f'results/{word_name}/{word_name}.png')
    plt.show()
