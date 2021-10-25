import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    URL = "https://api.twitter.com/2/tweets/search/recent"

    PARAMS = {
        'query': '#test -is:retweet lang:en',
        'tweet.fields': 'created_at',
        'max_results': 100
    }

    HEADERS = {
        "Authorization": f"Bearer {os.environ.get('BEARER_TOKEN')}",
        "User-Agent": "v2FullArchiveSearchPython"
    }

    REGEX_LIST = [
        "(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))",
        "(?<=^|(?<=[^a-zA-Z0-9-_\.]))@([A-Za-z]+[A-Za-z0-9-_]+)", "#", "[^A-Za-z0-9 | \n]+", "\t", "\n"
    ]


    