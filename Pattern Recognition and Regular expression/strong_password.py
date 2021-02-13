import re

strong_password = re.compile(r'''(
    ([A-z])
    [a-zA-Z0-9]+           #character class, upper, lower and numbers
                           #character for symbols

)''', re.VERBOSE)


mo = strong_password.search("pro244grammEr.")
print(mo.group())
