# https://www.nltk.org/index.html#

import nltk

sentence = "At eight o'clock on Thursday morning Arthur didn't feel very good."

tokens = nltk.word_tokenize(sentence)

list_of_token = []

for i in range (0, len(tokens)):
    list_of_token.append(tokens[i])

print(sentence, "is mapping to", list_of_token)
