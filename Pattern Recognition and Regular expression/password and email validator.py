import re
#creating a strong password validator function
def email_validator(email):
    #creating the email regex
    email_regex = re.compile(r'''(

    [a-zA-Z0-9._%+-]+           #username
    @                           #@ symbol
    [a-zA-Z0-9.-]+              #domain name
    (\.[a-zA-Z]{2,4})           #dot-something

    )''', re.VERBOSE)

    if email_regex.search(email):
        return f"{email} is a valid email"
    else:
        return f"{email} is not a valid email"


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
def strong_password_validator(password):
    while True:
        mo = strong_password.search(password)
        if (not mo):
            print("Your password should have at least one special charachter, two digits.")
            print("At least two uppercase and three lowercase charachter.")
            print("It Should be 8+ characters in lenght.")
            print("Enter another password:")
        else:
            print("Password is strong")
            return


password = input("Enter password to verify:")
email = input("Enter email to verify:")
email_validator(email)
strong_password_validator(password)
