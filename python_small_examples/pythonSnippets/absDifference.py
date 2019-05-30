'''
Given an int n, return
 the absolute difference between n and 21, 
 except return double the absolute difference if n is over 21.

diff21(19) - 2
diff21(10) - 11
diff21(21) - 0

'''

def abs_dif(n):
    
    if n > 21:
        ans2 = n - 21
        ans1 = ans2 * 2
    else:
        ans1 = 21 - n        
    return abs(ans1)
    
    
#ent = int(input('Enter number: '))
#value_diff = (abs_dif(ent))
#print(value_diff)
for i in range (1,50):
    
    print(i, ' --> ' ,abs_dif(i))
    