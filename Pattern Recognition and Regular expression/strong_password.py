import re

strong_password = re.compile(r'''(
    ^(?=.*[A-Z].*[A-Z])     # at least two characters
     (?=.*[!@#$&*])         # at least one of the special characters
     (?=.*[0-9].*[0-9])     # at least two numeric digits

)''', re.VERBOSE)


mo = strong_password.search("pro244grammEr.")
print(mo.group())
