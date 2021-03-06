'''
Program to count all the words in a user file

Accept a user file, and iterate through the full file, 
once done count occurrences of all the word in the file
Use a WITH OPEN statement instead of a FH Statement so you dont have to close the file

Steps:
Make a function with a dictionary to iterate.

Open a file in read mode
iterate through the full file
create a list to store all the contents in 
the file by eliminating  new line \n using extend clause
once all variables are done iterating, print the whole list


'''

import string
import sys
##use PPRINT to format the printed output nicely instead of print
from pprint import pprint 


def countCharacters(letters):
    ##declare a dictionary to store values
    charStorage ={}
    
    for n in letters:
        keys = charStorage.keys()
        #if the key is present for tht word add plus 1
        if n in keys:
            charStorage[n]+=1
        #if key not present in the word add key as 1
        else:
            charStorage[n]=1
    return charStorage

##use your CUSTOM FIle name here, and make sure it is in same folder or you reference the folder the file is in
with open('wikihow.txt', 'r') as fh:
    ##Create a list 
    listChars = []
## Append values of file to a list
## Pass that list to the function above

    for ch in fh:
    #listChars.append(ch.strip())
    ## Use this if you want to count occurrences of characters in the line        
    #listChars.extend(ch.strip())
    
    ## Use STRIP if you want to use to count words in a line
    ##USe STRIP to Return a copy of the string with the leading and trailing characters removed.
        listChars.extend(ch.split())
    
    
#print(listChars)
pprint(countCharacters(listChars))
    


