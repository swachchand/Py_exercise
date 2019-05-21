
"""
Even_Odd characters of String Printing:
Given a string, S, of N length  that is indexed from 0  
to N-1, print its even-indexed and odd-indexed characters
 as  2 space-separated strings on a single line
"""

def even_bits(str):
    result = ""  
    for i in range(len(str)):
        if i % 2 == 0:
            result = result + str[i]
    return result
def odd_bits(str):
    result = ""  
    for i in range(len(str)):
        if i % 2 == 1:
            result = result + str[i]
    return result


for i in range(int(input())):
    w = input('')    
    print(even_bits(w), ' ' ,odd_bits(w))

#############################################
"""
Short code using just slicing of lists

Uncomment code and add it in a new file
"""
############################################
#for i in range(int(input())):
#    w = input('')
#    print(w[::2], w[1::2])

