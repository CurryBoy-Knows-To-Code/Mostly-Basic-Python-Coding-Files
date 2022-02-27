# import re/regex/regular expressions is a library of code that supports weird charecters
import re
# this function asks the users input then passes the input to the function 'password_validation'


def user_input_password():
    print(" The password must be at least eight characters and must also contain at least one uppercase, lowercase and number and a special character.​")
    password = input("Enter your Password\n")
    return password
# this function validates the users password


def password_validation():
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    validation = False
    # This is a while loop which executes the tabulated lines below till line 37 and its always true unless you put a break statement
    while not validation:
        password = user_input_password()
        # this line will check if the length of the password you have inputed has at least 8 charecters
        if (len(password) < 8):
            print("Password length must be 8 charecters or more long ")
        # this line would check if the password has any charecter between a-z(lowercase)
        elif not re.search("[a-z]", password):
            print("Password does not contain any lowercase charecters")
        # this line would check if the password has any charecter between A-Z(uppercase)
        elif not re.search("[A-Z]", password):
            print("Password does not contain any uppercase letters")
        # this line would check if the password has any number between 0-9
        elif not re.search("[0-9]", password):
            print("Password does not contain any intergers")
        # this line checks if the password has special charecters
        elif (regex.search(password) == None):
            print("There is no special charecter")

        # if the password doesnt meet any of the statements above it means the inputed password is valid
        else:
            print("Valid password")
            validation = True


password_validation()
