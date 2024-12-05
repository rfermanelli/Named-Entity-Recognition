import spacy

nlp = spacy.load('it_core_news_sm')

l = []

frase = nlp("Il sistema deve gestire il flusso di email")
for token in frase:
    l.append(token)
    print(token, "|", token.pos_,"|", spacy.explain(token.pos_))

print(l)
