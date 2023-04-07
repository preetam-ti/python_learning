from email_validator import validate_email, EmailNotValidError

testEmail = "examplestackabuse.com"

try:
    # Validating the `testEmail`
    emailObject = validate_email(testEmail)

    # If the `testEmail` is valid
    # it is updated with its normalized form
    testEmail = emailObject.email
    print(testEmail)
except EmailNotValidError as errorMsg:
    # If `testEmail` is not valid
    # we print a human readable error message
    print(str(errorMsg))

"""import re

regex = re.compile(r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])")

def isValid(email):
    if re.fullmatch(regex, email):
        print("Valid email")
    else:
        print("Invalid email")

isValid("name.surname@gmail.com")
isValid("anonymous123@yahoo.co.uk")
isValid("anonymous123@...uk")
isValid("...@domain.us")

#############"""