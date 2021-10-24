from src.utilities.constants import Settings


def params_edit(next_token, word):
    Settings.PARAMS = {
        'query': f'#{word} -is:retweet',
        'tweet.fields': 'created_at',
        'next_token': next_token,
        'max_results': 100
    }


def parameter_updater(word):
    Settings.PARAMS = {
        'query': f'#{word} -is:retweet',
        'tweet.fields': 'created_at',
        'max_results': 100
    }
