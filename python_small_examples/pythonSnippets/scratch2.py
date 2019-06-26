### email and phone number scrapper from a dictionary

#! python3
'''
Create regex for phones
create regex for emails

get text off the keyboards

Extract email phones from text
copy email phone to clipboard
'''
import re
import pyperclip


## create regex for phone numbers:
phoneRegex = re.compile(r'''
#phone types 111-111-1111, 222-2222,(111) 111-1111, 111-222 ext 11111
(
((\d\d\d) | (\(\d\d\d\)))?    #area code optional
(\s|-)                        # first seperator
\d\d\d                        #first 3 DIGITS
-                             #seperator
\d\d\d\d                      #last 4 DIGITS
(((ext(\.)?\s)|x)
(\d{2,5}))                   #extensions x 11111 (optional)
)
''', re.VERBOSE)

#create regex for emails
emailRegex = re.compile(r'''
#example a@aa.com can have anything +, _, . etc
[a-zA-Z0-9_.+]+        #name part
@                      #@ symbol Part
[a-zA-Z0-9_.+]+        #Domain name part
''', re.VERBOSE)

# get text off the keyboards
textPaste = pyperclip.paste()

#Extract email phones from text
extractedPhNos = phoneRegex.findall(textPaste)
extractedEmailIds = emailRegex.findall(textPaste)


allPhones =[]
for phonenos in extractedPhNos:
    allPhones.append(phonenos[0])

#copy email phone to clipboard
print(allPhones)
print(extractedEmailIds)

results = '\n'.join(allPhones)+ '\n'+ '\n'.join(extractedEmailIds)
pyperclip.copy(results)
