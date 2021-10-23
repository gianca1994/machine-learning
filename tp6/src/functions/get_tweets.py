import requests
from src.utilities.constants import Settings
from src.utilities.parameter_editor import params_edit


def request_tweets(params):
    response = requests.get(url=Settings.URL, headers=Settings.HEADERS, params=params)
    if response.status_code == 200:
        return response.json()

def recopilation_tweets(num_page):
    tweets = []
    total_message = []
    while True:
        response = request_tweets(Settings.PARAMS)

        params_edit(response['meta']['next_token'])
        
        tweets.append(response['data'])

        num_page -= 1
        if num_page <= 0:
            for i in tweets:
                for j in i:
                    total_message.append(j)
            break

    return total_message