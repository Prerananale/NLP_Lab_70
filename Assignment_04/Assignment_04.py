from nltk import ngrams
from nltk.util import ngrams

#unigram model
n = 1
sentence = 'My native place is mumbai.'

unigrams = ngrams(sentence.split(), n)
print(f"\n***********   UNIGRAM    ************************")
for item in unigrams:
    print(item)
#bigram model
n = 2
sentence = 'My native place is mumbai.'

unigrams = ngrams(sentence.split(), n)
print(f"\n***********   BIGRAM    ************************")
for item in unigrams:
    print(item)

#trigram model
n = 3
sentence = 'My native place is mumbai.'
unigrams = ngrams(sentence.split(), n)
print(f"\n***********   TRIGRAM    ************************")
for item in unigrams:
    print(item)


