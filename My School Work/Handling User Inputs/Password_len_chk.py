def password_input():
    password1 = input("what is your password\n")
    password2 = input("\nwhat is your password again\n")
    return password1, password2


def password_validation():
    validpassword = False
    while not validpassword:
        password1, password2 = password_input()
        if (len(password1)) <= 8 or (len(password1)) >= 15:
            print("\nlength of password must be between 8 to 15\n")

        elif password1 != password2:
            print("\nnew password should be same as verification password\n")

        else:
            validpassword = True
            print("\ncorrect password\n")


password_validation()
