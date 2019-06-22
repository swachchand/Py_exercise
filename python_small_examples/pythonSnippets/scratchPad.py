## This file is a scratchpad can be used and changed as per practice codes
import re

'''
reptn = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){,}')
ph=input('Enter numbers:')

cmp =reptn.search(ph)
print(cmp.group())
'''

print('Testing all patterns of REGEX expression')

rgx = re.compile(r'\d\d\d-\d\d\d-\d\d\d')
rgxGrp = re.compile(r'\(\d\d\d\) (\d\d\d-\d\d\d\d)')
inpt= input('Enter an input:')

opt = rgx.search(inpt)
print(opt.group())

opt1 = rgxGrp.search(inpt)
print(opt1.group())


'''
Working on
+ * and ? patterns
? --> Pattern appears 0 or 1 time
* --> Pattern appears zero or more times
+ --> Pattern appears 1 or more times

'''
btrx = re.compile(r'mat(wo)?man') # For zero or 1 more time
btrx1 = re.compile(r'bat(wo)*man') # zero or more times
btrx3 = re.compile(r'bat(wo)+man') # zero or more times



opt2= btrx.search(inpt)
print(opt2.group())

opt3= btrx1.search(inpt)
print(opt3.group())


opt4= btrx3.search(inpt)
print(opt4.group())
