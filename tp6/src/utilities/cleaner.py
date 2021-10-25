from nltk.util import pr
from src.utilities.constants import Settings


def cleaner(dataframe):
    for i in Settings.REGEX_LIST:
        dataframe["text"].replace(i, '', regex=True, inplace=True)
    return dataframe
