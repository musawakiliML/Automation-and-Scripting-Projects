import re

strong_password = re.compile(r'''(
    ^(?=.*[A-Z].*[A-Z])     # at least two characters
     (?=.*[!@#$&*])         # at least one of the special characters
     (?=.*[0-9].*[0-9])     # at least two numeric digits
     (?=.*[a-z].*[a-z].*[a-z]) # at least three lower case characters
     .{8,}                     # at least a total of eight characters 
     $
)''', re.VERBOSE)


mo = strong_password.search("pro244grammEr.")
print(mo.group())
