import nltk


def labeling(words, word):
    pos_labeling = []
    for i in words:
        for j in i:
            pos_labeling.append(j)
    all_words = " ".join(map(str.lower, pos_labeling))

    text_tokens = nltk.word_tokenize(all_words)
    text_pos = nltk.pos_tag(text_tokens)

    file = open (f'results/{word}/{word}-POS-Adjetives.csv', 'w')
    for i in text_pos:   
        if i[1] in ['JJ', 'JJR', 'JJS']: 
            file.write('Word:' + i[0] + ', ' + 'POS:' + i[1] + '\n')
    file.close()

    file = open (f'results/{word}/{word}-POS-Nouns.csv', 'w')
    for i in text_pos:   
        if i[1] in ['NN', 'NNP', 'NNPS']: 
            file.write('Word:' + i[0] + ', ' + 'POS:' + i[1] + '\n')
    file.close()
