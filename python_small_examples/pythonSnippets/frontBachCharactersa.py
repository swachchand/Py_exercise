'''
Given a string, return a new string 
where the first and last chars have been exchanged.

However this program also changes only 1st and last character of a string, 
if there are multiple words in the string it changes only first and last Characetr of those words
'''


def front_back(s1):
    if len(s1) == 1:
        return s1
    else:
        newlist = []
        convert_to_list = s1.split()
        for each in convert_to_list:
            each_list = list(each)
            firstC, lastC = each_list[0], each_list[-1]

            each_list[0] = lastC
            each_list[-1] = firstC

            newword = ''.join(each_list)
            newlist.append(newword)


    return ' '.join(newlist)

inpt1 = input('Enter string :')
print(front_back(inpt1))