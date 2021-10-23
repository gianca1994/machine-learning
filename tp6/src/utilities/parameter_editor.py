from src.utilities.constants import Settings

def params_edit(next_token):
    Settings.PARAMS = {
    'query': '#charlygarcia -is:retweet',
    'tweet.fields':'created_at',
    'next_token': next_token,
    'max_results':100
    }