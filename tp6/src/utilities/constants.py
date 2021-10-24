import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    URL = "https://api.twitter.com/2/tweets/search/recent"

    PARAMS = {
        'query': '#test -is:retweet',
        'tweet.fields': 'created_at',
        'max_results': 100
    }

    HEADERS = {
        "Authorization": f"Bearer {os.environ.get('BEARER_TOKEN')}",
        "User-Agent": "v2FullArchiveSearchPython"
    }
