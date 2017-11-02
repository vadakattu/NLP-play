import glob
import spacy
import ipdb
from collections import Counter

docs = {}
sentences = []
nlp = spacy.load('en')

for txt in glob.glob("*.txt"):
    docs[txt] = nlp(open(txt).read())
    sentences += list(docs[txt].sents)

words = []
for doc in docs.items():
    # Removing punctuation and common "stop words"
    tokens = [token.text for token in doc[1] if token.is_stop == False and token.is_punct == False]
    words += [w for w in tokens if w.isalnum() == True]


word_freq = Counter(words)

for word in word_freq.most_common(1):
    print([sent for sent in sentences if sum([word[0] == token.lower_ for token in sent]) > 0])

