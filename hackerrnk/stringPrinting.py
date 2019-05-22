
"""
Even_Odd characters of String Printing:
Given a string, S, of N length  that is indexed from 0  
to N-1, print its even-indexed and odd-indexed characters
 as  2 space-separated strings on a single line
"""

def even_bits(str1):
    result = ""  
    for i in range(len(str1)):
        if i % 2 == 0:
            result = result + str1[i]
    return result
def odd_bits(str1):
    result = ""  
    for i in range(len(str1)):
        if i % 2 == 1:
            result = result + str1[i]
    return result

ip_lst = [] # input list that contains all input strings

for i in range(int(input())):
    w = input('')
    ##print(w[::2], w[1::2])
    ip_lst.append(w)

for inp in ip_lst:
    print(even_bits(inp), ' ', odd_bits(inp))

#############################################
"""
Short code using just slicing of lists

Uncomment code and add it in a new file
"""
############################################
#for i in range(int(input())):
#    w = input('')
#    print(w[::2], w[1::2])

