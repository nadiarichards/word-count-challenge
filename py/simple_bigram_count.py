import re
from collections import Counter

def bigram_counter(text_file):

    words = re.findall('\w+', open(text_file).read())
    bigram_counter=Counter(zip(words, words[1:]))

    for k, v in bigram_counter.items():
        if v >= 2:
            print (k, ':', v)

bigram_counter('../sample3.txt')