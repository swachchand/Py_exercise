'''
Given a non-empty string like "Code" return a string like "CCoCodCode".

string_splosion('Code') - 'CCoCodCode'
string_splosion('abc') - 'aababc'
string_splosion('ab') - 'aab'

'''
def string_splosion(s):
    i, result = 0, ''
    while i < len(s):
        i += 1
        result += s[:i]
    return result

s1 = input('Enter: ')
print(string_splosion(s1))
      
      
    

