import re

strong_password = re.compile(r'''(
    [a-zA-Z0-9]+        #character class, upper, lower and numbers
    [@+\%_|-|\.$]+          #character for symbols
)''', re.VERBOSE)

mo = strong_password.search("pro244grammer.")
print(mo.group())
