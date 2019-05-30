'''
Given a string, 
we'll say that the front is the first 3 chars of the string. .
If the string length is less than 3, the front is whatever is there. 
Return a new string which is 3 copies of the front.

front3('Java') 'JavJavJav'
front3('Chocolate')  'ChoChoCho'
front3('abc') -- 'abcabcabc'
front3('abcXYZ')  'abcabcabc'    
front3('ab') 'ababab'        
front3('a') 'aaa'    
front3('')  ''

'''

def front3(strChars):
    if len(strChars) == 3:        
        return strChars * 3
    else:
        mkList = list(strChars)
        tmpList = mkList[:3]
        strChars =''.join(tmpList)
        return strChars * 3


inpt1 = input('Enter word:')
print(front3(inpt1))