'''
Given a string, return a new string 
where the first and last chars have been exchanged.

front_back('code') -- 'eodc'
front_back('a') -- 'a'
front_back('ab') -- 'ba'

'''

def front_back(s1):
    if len(s1) == 1:
        return s1
    else:
        convert_to_list = list(s1)
        temp_list = convert_to_list[0], convert_to_list[-1]
        convert_to_list[-1] = temp_list[0]
        convert_to_list[0] = temp_list[1]
        s1 = ''.join(convert_to_list)
        return s1

inpt1 = input('ENter string :')
print(front_back(inpt1))
