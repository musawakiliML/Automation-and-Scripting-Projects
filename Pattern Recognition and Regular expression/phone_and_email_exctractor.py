import re, pyperclip
# create a phone number regex
phone_num_regex = re.compile(r'''(
    [+]?                         #+ sign for the area code
    (\d{3}|\(\d{3}\))?          #areacode
    (\s|-|\.)?                  #seperator
    (\d{3})                     #first three characters
    (\s|-|\.)                   #seperator
    (\d{3})                     #second 3 numbers
    (\s|-|\.)                   #seperator
    (\d{4})                     #last 4 digits
)''', re.VERBOSE)

#mo = phone_num_regex.search("+234-813-581-0804")
#print(mo.group())

# creating an email regex
email_regex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+           #username
    @                           #@ symbol
    [a-zA-Z0-9.-]+              #domain name
    (\.[a-zA-Z]{2,4})           #dot-something
)''', re.VERBOSE)

#mo1 = email_regex.search("musawakiliml1@gmail.com")
#print(mo1)

# finding match in clipboard text.
text = str(pyperclip.paste())

matches = [] # creating an empty list
# finding all the matching phone number
for groups in phone_num_regex.findall(text):
    phone_num_regex = '-'.join([groups[1],groups[3],groups[5],groups[7]])
    matches.append(phone_num_regex)

# finding all the matching email address
for groups in email_regex.findall(text):
    matches.append(groups[0])

# copy result to the clipboard
if len(matches) > 0:
    pyperclip.copy("\n".join(matches))
    print("Copied to clipboard")
    print("\n".join(matches))
else:
    print("No phone number of email found")

