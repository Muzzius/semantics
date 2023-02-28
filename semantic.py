import spacy
nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

"""
Cat and monkey have an above average similarity, probably because they are
both animals, and both mammals. The same is true for apple and banana, they
have high similarity to each other as they are both fruit


Monkey and banana have higher similarity the monkey and apple, probably
because monkeys are commonly depicted as enjoying bananas. The same 
connection does not exist between monkey and apple despite both of them 
being fruit so there is lower similarity. Highlighting that this comparison
does not take into account transitive relations.

Cat has low similarity to both bananas and apples which is expected as cats
are not really associated with either fruit. Cat and banana are more similar
than cat and apple but I am not really sure why this is the case.
"""

sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
             "Hello, there is my car",
             "I\'ve lost my car in my car",
             "I\'d like my boat back",
             "I will name my dog Diana"
             ]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

"""
Running example.py with the mode en_core_web_sm instead of en_core_web_md gave the following warning when checking
the similarities between strings:

UserWarning: [W007] The model you're using has no word vectors loaded, 
so the result of the Doc.similarity method will be based on the tagger,
parser and NER, which may not give useful similarity judgements. 
This may happen if you're using one of the small models, e.g. `en_core_web_sm`,
which don't ship with word vectors and only use context-sensitive tensors. 
You can always add your own word vectors, or use one of the larger models
instead if available.

One of the main differences I can see in the output is that the results for
the similarity between two tokens is lower except for exact matches which still
give 1.
"""