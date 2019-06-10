'''
Print entire character stream in reverse 
without ---> List Comprehension Technique (simple traditional for loop)
example:
hello world
olleh dlrow
'''

word = input('Enter: ')
##The split() method splits a string into a list.
w = word.split(' ')



re =[]
for i in w:
    re=i[::-1]
    #re.append()
    print(re, end=' ')


#print(re)