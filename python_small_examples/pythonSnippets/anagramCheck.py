'''
CHeck if the strings are Anagrams of each other
'''

def anagram_chk(s1, s2):
    #First convert the words to lowe case
    w1=list(s1.lower())
    w2= list(s2.lower())
    ##Sort the strings alphabetically
    sort1 = sorted(w1)
    sort2 = sorted(w2)
    ##Compare the strings if they are equal and if they're equal they are anagrams, if not then not anagrams
    if sort1 == sort2:
        return ''.join(sort1), ' and ', ''.join(sort2), 'are anagrams of each other'
        ##return sort1, ' and ', sort2, ' are anagrams of each other'
    else:
        return 'you are NOOOTTTTT the ANAGRAM.......!!!!!'



st1 = input('enter string 1: ')
st2 = input ('enter str 2: ')
print(anagram_chk(st1, st2))








