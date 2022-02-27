import re
import os
# re is used to basically validate a certain format such as we have to validate the format of the email


def reseting_files():
    # we use the files list of invalid email addresses and list of valid email addresses to seperate the valid and invalid emails
    # after that is shown we have to reset the files for a new set of emails
    # but if we remove the files which has not been created yet it raises a FileNotFoundError so we catch it

    try:
        os.remove("list of invalid email addresses")
        os.remove("list of valid email addresses")
        validating_list_of_email_addresses()
    except FileNotFoundError:
        validating_list_of_email_addresses()


def validating_list_of_email_addresses():
    # this fuction is csalled if you have a list of email addresses to be  validated
    invalid_list_name = "list of invalid email addresses"
    valid_list_name = "list of valid email addresses"
    valid_choice = False
    # check if the file exists if it doesnt asks the user to type the file name again
    while not valid_choice:
        users_file = input(
            "what is the file name with the list of email addresses\n")
        check = os.path.exists(users_file)
        if check == True:
            print(
                "\nValid emails in the file are written in a new file called 'list of valid emails'\n")
            print(
                "Invalid emails in the file are written in a new file called 'list of invalid emails'\n")
            # this is the typical format of a email
            # basically in order 'a-zA-Z0-9' in the pattern means any charecter from a - z and A - Z and any number to 0-9
            # the + @ means there must be a @ symbol after typing the username and after that type your domain name then your domain
            pattern = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|net|co.uk)"
            valid_choice = True
            datafile = open(users_file, "r")
            for list_of_emails in datafile:
                # we see here the re is used to check if the input meets the pattern
                valid_email = re.search(pattern, list_of_emails)
                if bool(valid_email) == True:
                    # valid emails are put in the file 'list of valid email addresses' and invalid emails are put in the file 'list of invalid email addresses'
                    # have to open in append mode because thats the only way the older valid and invalid emails are there
                    list_of_valid_emails = open(valid_list_name, "a")
                    list_of_valid_emails.write("{}\n".format(list_of_emails))
                    list_of_valid_emails.close()
                elif bool(valid_email) == False:
                    list_of_invalid_emails = open(invalid_list_name, "a")
                    list_of_invalid_emails.write("{}\n".format(list_of_emails))
                    list_of_invalid_emails.close()
                # after looping through all the files
        elif check == False:
            print("this file does not exist")


def where_email_is_typed_and_validated():
    valid = False
    # we use re to check if the email is valid , same as the pattern but we have split it so that the program point out specifically what is wrong
    while not valid:
        user_email = input("enter your email address\n")
        if not re.search("[a-zA-Z0-9]", user_email):
            print("your email address does not have a username before the @ gmail")
        elif not re.search("[a-zA-Z0-9]+@", user_email):
            print("your email address does not have a @ symbol")
        elif not re.search("[a-zA-Z0-9]+@[a-zA-Z]", user_email):
            print("your email address does not have a domain name")
        elif not re.search("[a-zA-Z0-9]+@[a-zA-Z]+\.", user_email):
            print("Your email address does not have a . after its domain name")
        elif not re.search("[a-zA-Z0-9]+@[a-zA-Z]+\.(com|net|co.uk)", user_email):
            print("Your email address does not have a domain")
        else:
            valid = True
            print("Valid email")
            user_choice()


def user_choice():
    # here you get to choose what you want to do and again there is validation
    valid_and_choice = False
    while not valid_and_choice:
        print("Press 1 if you want to validate your own email address")
        print("Press 2 if you want to validate a list of email addresses")
        print("Press 3 if you want to quit the game")
        user_choice = input("Which number do you choose\n")
        if user_choice == "1":
            where_email_is_typed_and_validated()
        elif user_choice == "2":
            reseting_files()
        elif user_choice == "3":
            print("Good bye")
            exit()
        else:
            print("Invalid choice")


user_choice()
