import re
reptn = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){,}')
ph=input('Enter numbers:')

cmp =reptn.search(ph)
print(cmp.group())
