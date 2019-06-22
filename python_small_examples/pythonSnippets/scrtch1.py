import re

'''
? --> Pattern appears 0 or 1 time
* --> Pattern appears zero or more times
+ --> Pattern appears 1 or more times
{} is used for minimun and maximum matches in the sentence
{1,5} means 1 minimum and 5 times maximum, blank with a comma {,} is 0 min,max
\d is DIGITS
\D is Any char that is not a numeric from 0-9
\w any letter numeric digit an underscore character
\W Any character that is not a letter, numeric digit or underscore character
\s is a space tab
\S is not a space
^ in the [] is used to find all other than expressed in the input

^ in a string is used to check if pattern occurs at the begning of the string
and $ is used to check if it occurs at the end of the string
e.f.(r'^Hppp$')
. character (dot/period) stands for any character except a new line

'''
inpt = 'Hello, Robocop is a dodo, trust me I AM NOT an engineer,11 people sss, 332 peoplr are ,23232 mine eee, 44 times www, 1 peart or, 33 frits'

sRgx = re.compile(r'\d+\s\w+')
print(sRgx.findall(inpt))

voRx = re.compile(r'[aeiouAEIOU]')
#voRx = re.compile(r'[^aeiouAEIOU]')
#voRx = re.compile(r'[^A-Za-z]')
print(voRx.findall(inpt))

ptrnRgx = re.compile(r'^[A-Z]+')
chk = 'POP my name is woeuf'
print(ptrnRgx.search(chk))
