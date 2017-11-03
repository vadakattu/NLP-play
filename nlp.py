import glob
import spacy
from collections import Counter
import pandas as pd

docs = {}
nlp = spacy.load('en')

for txt in glob.glob("*.txt"):
    docs[txt] = nlp(open(txt).read())

words = []
for doc in docs.items():
    # Removing punctuation and common "stop words"
    tokens = [token.lower_ for token in doc[1] if token.is_stop == False and token.is_punct == False]
    words += [w for w in tokens if w.isalnum() == True]

# find most common words across all documents
word_freq = Counter(words)

top_n = 20
results = []
for word in word_freq.most_common(top_n):
    for doc in docs.items():
        sentences = [sent for sent in doc[1].sents if sum([word[0] == token.lower_ for token in sent]) > 0]
        for s in sentences:
            results.append((' - '.join(map(str, word)), doc[0], s))

df = pd.DataFrame.from_records(results, columns=('Word - Frequency', 'Document', 'Sentence'))
df.to_excel('top_%s_results.xlsx' % top_n, index=False)