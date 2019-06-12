
'''
to display array excluding duplicates
'''

def remDups (ary):
    ##Create empty list
    nd = []
    #traverse original input 
    for i in ary:
        ##If element not present in the new empty list append it to the new list
        if i not in nd:
            nd.append(i)
    return nd

a1= input('Enter values: ')
print(remDups(a1))


###2nd option 1 liner
#inpt = ['h', 'h', 'e', 'e', 'l', 'l', 'o', 'o']
inpt = input('Enter string: ')
print('Original String:', inpt, '\n')
#Command to remove duplicates
ip = list(dict.fromkeys(inpt))

ip.sort()
print('\nBefore showing it as a string: ',ip ,'\n')
print(''.join(ip))

#print(ip.append())