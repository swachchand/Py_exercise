'''
Given an int n, 
return True if it is within 10 of 100 or 200. 
Note: abs(num) computes the absolute value of a number.

near_hundred(93)  True
near_hundred(90)   True
near_hundred(89)   False
'''


def near_hundred(n):
  if abs(100 - n) <= 10 or abs(200 - n) <= 10:
    return True
  else:
    return False
    
print('Given an int n, \n return True if it is within 10 of 100 or 200.\n Note: abs(num) computes the absolute value of a number. \n examples: \n near_hundred(93)  True \n near_hundred(90)   True \n near_hundred(89)   False \n \n')

ip = int(input('Enter Number: '))

print(ip, '--> ',near_hundred(ip))