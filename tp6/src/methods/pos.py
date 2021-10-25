import nltk


def labeling(words):
    pos_labeling = []
    for i in words:
        for j in i:
            pos_labeling.append(j)
    all_words = " ".join(map(str.lower, pos_labeling))

    text_tokens = nltk.word_tokenize(all_words)

    text_pos = nltk.pos_tag(text_tokens)

    return text_pos
