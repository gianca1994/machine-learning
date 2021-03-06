from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

def polarity(dataframe, word_name):
    sentiment_analyzer = SentimentIntensityAnalyzer()
    dataframe["negative"], dataframe["neutral"], dataframe["positive"], dataframe["result"] = "", "", "", ""
    negative, positive, neutral = 0, 0, 0

    for index, row in dataframe.iterrows():
        analisis = sentiment_analyzer.polarity_scores(row['text'])
        row["negative"], row["neutral"], row["positive"] = analisis["neg"], analisis["neu"], analisis["pos"]
        
        if 1 >= analisis['compound'] > 0.15:
            row["result"] = "Positive"
            positive += 1
        elif -0.15 > analisis['compound'] >= -1:
            row["result"] = "Negative"
            negative += 1
        else :
            row["result"] = "Neutral"
            neutral += 1

    ranges = ["Positive","Negative","Neutral"]
    colores = ["#EE6055","#60D394","#AAF683","#FFD97D","#FF9B85"]
    plt.pie(dataframe['result'].value_counts().tolist(), labels=ranges, autopct="%0.1f %%", colors=colores)
    plt.axis("equal")
    plt.savefig(f'results/{word_name}/{word_name}-polarity.png')
    plt.show()

    dataframe.to_csv(f'results/{word_name}/{word_name}-PolarityAnalysis.csv')
    