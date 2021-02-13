import re

# creating the strong password regex
strong_password = re.compile(r'''(
    ^(?=.*[A-Z].*[A-Z])     # at least two characters
     (?=.*[!@#$&*])         # at least one of the special characters
     (?=.*[0-9].*[0-9])     # at least two numeric digits
     (?=.*[a-z].*[a-z].*[a-z]) # at least three lower case characters
     .{8,}                     # at least a total of eight characters 
     $
)''', re.VERBOSE)

# creating the strong password validator function
def strong_password_validator():
    print("Enter a password:")
    while True:
        password_input = input()
        mo = strong_password.search(password_input)
        if (not mo):
            print("Your password should have at least one special charachter, two digits.")
            print("At least two uppercase and three lowercase charachter.")
            print("It Should be 8+ characters in lenght.")
            print("Enter another password:")
        else:
            print("Password is strong")
            return
strong_password_validator()