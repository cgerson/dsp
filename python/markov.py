#!/usr/bin/env 

import random
import sys

EOS = ['.', '?', '!']

"""        
def __init__(self, open_file):
                self.cache = {}
                self.open_file = open_file
                self.words = self.file_to_words()
                self.word_size = len(self.words)
                self.database()
"""                
      
def file_to_words(text):

    words = text.split()
    return words
               
        
def database(words):
    """ Generates triples from the given data string. So if our string were
                                "What a lovely day", we'd generate (What, a, lovely) and then
                                (a, lovely, day).
    """

    d={}
    if len(words) < 3:
        return
                
    for i in range(len(words) - 2):
        first,second,third = (words[i], words[i+1], words[i+2])
                        
        key = (first,second)
        if key not in d:
            d[key] = []
        d[key].append(third)
                        
        return d
                                
def generate_markov_text(d, size=40):

    """
                seed = random.randint(0, len(d)-3)
                seed_word, next_word = d[seed], d[seed+1]
                w1, w2 = seed_word, next_word
    """

    li = [key for key in d.keys() if key[0][0].isupper()]
    key = random.choice(li)
 
    li = []
    first, second = key
    li.append(first)
    li.append(second)
    
    while len(li)<size:
        try:
            third = random.choice(d[key])
        except KeyError:
            break
        li.append(third)
        if third[-1] in EOS:
            break
        key = (second, third)
        first, second = key
    
    return ' '.join(li)

def main():

    fname = sys.argv[1]
    size_sent = int(sys.argv[2])
    with open(fname, "rt") as f:
        text = f.read()
    words = file_to_words(text)
    d = database(words)
    output = generate_markov_text(d,size=size_sent)
    print output

if __name__ == "__main__":

    if len(sys.argv) == 1:
        print("Error: provide an input corpus file.")
        sys.exit(1)
    # else
    main()

