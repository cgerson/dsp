#!/usr/bin/env python 

import pickle
import random
 
fh = open("stories.txt", "r")
 
chain = {}
 
def generate_trigram(words):
    if len(words) < 3:
        return
    for i in xrange(len(words) - 2):
        yield (words[i], words[i+1], words[i+2])
 
for line in fh.readlines():
    words = line.split()
    for word1, word2, word3 in generate_trigram(words):
        key = (word1, word2)
        if key in chain:
            chain[key].append(word3)
        else:
            chain[key] = [word3]
 
pickle.dump(chain, open("chain.p", "wb" ))

chain = pickle.load(open("chain.p", "rb"))
 
new_review = []
sword1 = "BEGIN"
sword2 = "NOW"
 
while True:
    sword1, sword2 = sword2, random.choice(chain[(sword1, sword2)])
    if sword2 == "END":
        break
    new_review.append(sword2)
 
print ' '.join(new_review)
