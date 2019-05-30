
'''
Given a non-empty string like 

"Code" return a string like "CCoCodCode".

string_splosion('Code')-- 'CCoCodCode'
string_splosion('abc') -- 'aababc'
string_splosion('ab') -- 'aab'
'''

def string_Splosion(st):
    result = '' ## To store strings starting form character 1 to the end of string
    # On each iteration, add the substring of the chars 0..i
    for i in range(len(st)):
        result = result + st[:i+1] + ' ' ## Seperate the splosion by a space and store it in result
    return result

inp = input('Enter String: ')
oup = string_Splosion(inp)
print(oup)

