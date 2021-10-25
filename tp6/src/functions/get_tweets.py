from nltk.util import pr
import requests
from src.utilities.constants import Settings
from src.utilities.parameter_editor import params_edit
import pandas as pd

def request_tweets(params):
    response = requests.get(url=Settings.URL, headers=Settings.HEADERS, params=params)
    if response.status_code == 200:
        return response.json()


def recopilation_tweets(num_pages, word, lang):
    tweets = []
    total_message = []

    while True:
        response = request_tweets(Settings.PARAMS)

        num_pages -= 1
        if num_pages <= 0 or len(response['meta']) <= 3:
            tweets.append(response['data'])
            for i in tweets:
                for j in i:
                    total_message.append(j)
            break

        params_edit(response['meta']['next_token'], word, lang)
        tweets.append(response['data'])

    return total_message
