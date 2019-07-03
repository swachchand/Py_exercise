'''
Check if a string is a palindrome or not
'''

#reverse the given string:

def reverse(s):
    return s[::-1]

#Check if the reverse string is equal to the actual string
def isPalin(s):
    rev = reverse(s)
    if (s==rev):
        return True
      
    return False

inp = input('Enter string: ')

opt = isPalin(inp)

if opt ==1:
    print(inp, 'is Palindrome')
else:
    print(inp, ' is not palindrome')


    