'''
Given a non-empty string and an int n, 
return a new string where the char at index n has been removed. 
The value of n will be a valid index of a char 
in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).

missing_char('kitten', 1)  'ktten'
missing_char('kitten', 0)  'itten'
missing_char('kitten', 4)  'kittn'

'''

def missing_char(st1, n):
    ### Make a List and move the string to the list
    l = list(st1)
    ### Delete the designated charater index    
    del(l[n])
    ##move the List back to string
    st1 = ''.join(l)
    return st1
