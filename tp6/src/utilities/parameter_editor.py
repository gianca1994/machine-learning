from src.utilities.constants import Settings


def params_edit(next_token, word, lang):
    Settings.PARAMS = {
        'query': f'#{word} -is:retweet lang:{lang}',
        'tweet.fields': 'created_at',
        'next_token': next_token,
        'max_results': 100
    }


def parameter_updater(word, lang):
    Settings.PARAMS = {
        'query': f'#{word} -is:retweet lang:{lang}',
        'tweet.fields': 'created_at',
        'max_results': 100
    }
