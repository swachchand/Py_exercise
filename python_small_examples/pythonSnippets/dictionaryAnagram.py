'''
Create a dictionary of 
(sorted word, list of word).
All the words that are in the same 
list are anagrams of each other.
'''

from collections import defaultdict

def load_words(filename=''):
    with open(filename) as f:
        for word in f:
            yield word.rstrip()

def get_anagrams(source):
    d = defaultdict(list)
    for word in source:
        key = "".join(sorted(word))
        d[key].append(word)
    return d

def print_anagrams(word_source):
    d = get_anagrams(word_source)
    for key, anagrams in d.iteritems():
        if len(anagrams) > 1:
            print(key, anagrams)

word_source = load_words()
print_anagrams(word_source)