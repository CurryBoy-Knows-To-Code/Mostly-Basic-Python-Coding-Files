import re


def password_reset(old_password, new_password, list_of_details):
    # here is where you change your old password to your new password
    # finds the index of the old password then repaces it with the new password then  writes the new password to the file and then quits the program
    for index in range(len(list_of_details)):
        if list_of_details[index] == ("password:"+old_password):
            list_of_details[index] = "password:"+new_password
            datafile = open("user names and their passwords", "w")
            for details in list_of_details:
                datafile.write("\n{}".format(details))
            datafile.close()
            print("password has been changed")
            exit()


def password_strength_checker(old_password, new_password, list_of_details):
    # basically i have a key which determines how strong ypur password is after that you have a choice if you want to change ypu password or keep the same password and reset it and for that there is also validation
    no_of_special_charecters = digits = alphabets = 0
    for letters in range(len(new_password)):
        if(new_password[letters].isalpha()):
            alphabets = alphabets + 1
        elif(new_password[letters].isdigit()):
            digits = digits + 1
        else:
            no_of_special_charecters += 1

    if (len(new_password) >= 8) and (len(new_password) < 12) and no_of_special_charecters == 0:
        print("You have a weak password")
    elif (len(new_password) >= 12) and (len(new_password) < 18) and no_of_special_charecters >= 1 and no_of_special_charecters <= 3:
        print("You have a medium password")
    elif (len(new_password) >= 18) and (len(new_password) < 24) and no_of_special_charecters > 3 and no_of_special_charecters < 5:
        print("You have a strong password")
    elif (len(new_password) >= 24) and (no_of_special_charecters >= 5):
        print("You have a super strong password")

    valid = False
    while not valid:
        print("Press 1 if you still want to reset your password")
        print("Press 2 if you want change your password")
        choice = input("Which number do you choose\n")
        if choice == "1":
            password_reset(old_password, new_password, list_of_details)
        elif choice == "2":
            password_reset_check(old_password, list_of_details)
        else:
            print("Invalid choice")


def password_validation(user_password, old_password, list_of_details):
    # validates the password and checks if it has caps small case and numbers
    if len(user_password) < 8:
        print("Password must be at least 8 ")
        password_reset_check(old_password, list_of_details)
    elif not re.search("[a-z]", user_password):
        print("doesnt have lower case letters")
        password_reset_check(old_password, list_of_details)
    elif not re.search("[A-Z]", user_password):
        print("doesnt have upper case letters")
        password_reset_check(old_password, list_of_details)
    elif not re.search("[0-9]", user_password):
        print("doesnt have any numbers")
        password_reset_check(old_password, list_of_details)
    else:
        print("valid")
        return user_password


def password_reset_check(old_password, list_of_details):
    valid = False
    while not valid:
        # we get the password that is going to be the new one  which is also going to be validated
        user_input1 = input("Enter your new password\n")
        password1 = password_validation(
            user_input1, old_password, list_of_details)
        password2 = input(
            "enter the same password to make sure you typed it correctly\n")
        # you have to type the same password then if you do you can choose if you want to see how string your password is or  you can just reset your password
        if password1 != password2:
            print("both passwords dont match")
        elif password1 == password2:
            print("user password is correct")
            while not valid:
                print("Press 1 if you want to see the strength of your password, after seeing the strength of your password you can choose to continue and reset password or change it again\n")
                print("Press 2 if just want to reset password")
                choice = input("Which number do you choose\n")
                if choice == "1":
                    password_strength_checker(
                        old_password, password1, list_of_details)
                elif choice == "2":
                    password_reset(old_password, password1, list_of_details)
                else:
                    print("Invalid choice")


def user_name_and_old_password_check():
    # we ask the user the their username which is in a filenand see if that username exists
    list_of_details = []
    valid = False
    while not valid:
        users_user_name = input("Enter your user name\n")
        if users_user_name == "password" or users_user_name == "username":
            print("Only type your user name")
        else:
            datafile = open("user names and their passwords.txt", "r")
            # we do this by looping through the list to see if it exists and the the info in the file is appended to a list
            for details in datafile:
                x = details.strip()
                list_of_details.append(x)
            datafile.close()
            if ("username:"+users_user_name) in list_of_details:
                print("username exists")
                # if the user name does exist then we ask the  password corresponding to it then if it is correct we the can change the password by calling the function 'password_reset_chec()'
                while not valid:
                    old_password = input(
                        "to reset your password enter your old password\n")
                    if ("password:"+old_password) in list_of_details:
                        print("valid old password")
                        password_reset_check(old_password, list_of_details)
                    else:
                        print("incorrect password")
            else:
                print("it doesnt exist")


user_name_and_old_password_check()
