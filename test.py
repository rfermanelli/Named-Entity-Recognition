# https://www.nltk.org/index.html#

import nltk

sentence = "At eight o'clock on Thursday morning Arthur didn't feel very good."

tokens = nltk.word_tokenize(sentence)

for i in range (0, len(tokens)):
    print(tokens[i])
