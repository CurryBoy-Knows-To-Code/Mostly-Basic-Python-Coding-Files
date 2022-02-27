import os


def save_list_names_in_a_file(list_of_names):
    # here you save the list of names by opening in write mode but before that it checks if the file exists thats why you use os
    valid_file = False
    while not valid_file:
        filename = input("What is the name of your file\n")
        if os.path.exists(filename):
            print("this file exists, create a new file for a new set of names")
        else:
            valid_file = True
            datafile = open(filename, "w")
            # we loop through the names and write it to the users chosen file
            for names in list_of_names:
                datafile.write("\n{}".format(names))
            datafile.close()
            print("data has been added to the file :", filename)


def what_the_user_wants_to_do_with_list_of_names(list_of_names):
    # if the user didnt type any name then the function is called where they can type the names to the list
    if len(list_of_names) == 0:
        print("there is no input")
        where_the_user_types_names(list_of_names)
    valid = False
    while not valid:
        # here is where you can do many things with the list of names
        print("Press 1 if you want to see the list of names")
        print("Press 2 if you want to see the list of names in reverse")
        print("Press 3 if you want to see a specific name in the list")
        print("Press 4 if you want to see a specific range of names")
        print("Press 5 if you want to remove a specific name in a list")
        print("Press 6 if you want to add more names to the list")
        print("Press 7 if you want save the list of names")
        print("Press 8 if you want to go back to the menu")
        user_choice = input("Which number do you choose\n")
        if user_choice == "1":
            for names in list_of_names:
                print(names)
        elif user_choice == "2":
            # reversed basicaly reverses the oder in which it is printed
            for names_in_reverse in reversed(list_of_names):
                print(names_in_reverse)
        elif user_choice == "3":
            valid1 = False
            while not valid1:
                # you type which number you want to see corresponding to the name
                print("the no of items in you list is", len(list_of_names))
                user_index = input("Enter the number\n")
                if user_index.isnumeric():
                    if int(user_index) < 1 or int(user_index) > len(list_of_names):
                        print("Invalid choice")
                    else:
                        print(list_of_names[int(user_index) - 1])
                        valid1 = True
                else:
                    print("Invalid choice")
        elif user_choice == "4":
            valid2 = False
            while not valid2:
                # print a specific range of names by using a for loop
                print("the no of items in you list is", len(list_of_names))
                print("choice includes the starting number and ending number")
                start = input("Enter your starting number\n")
                end = input("Enter your ending number\n")
                if start.isnumeric() and end.isnumeric():
                    if int(start) < 1 or int(end) < 1 or int(start) > len(list_of_names) or int(end) > len(list_of_names) or int(start) > int(end):
                        print("Invalid choice")
                    else:
                        for names in list_of_names[int(start) - 1:int(end)]:
                            print(names)
                        valid2 = True
                else:
                    print("Invalid choice")
        elif user_choice == "5":
            valid3 = False
            # we remove the name using the pop method
            while not valid3:
                print("the no of items in you list is", len(list_of_names))
                user_index = input("Enter the item number in list to remove\n")
                if user_index.isnumeric():
                    if int(user_index) < 1 or int(user_index) > len(list_of_names):
                        print("Invalid choice")
                    else:
                        list_of_names.pop(int(user_index) - 1)
                        valid3 = True
                else:
                    print("Invalid choice")
        elif user_choice == "6":
            # here you can add more list of names
            valid = True
            where_the_user_types_names(list_of_names)
        elif user_choice == "7":
            # calls the function to save the list of names
            valid = True
            save_list_names_in_a_file(list_of_names)
        elif user_choice == "8":
            # this function is to go back to the main menu
            valid = True
            main_menu()
        else:
            print("Invalid choice")


def get_names_from_users_file(list_of_names):
    # if the user has a file with a list of names here it is checked whether it exists or not
    tries = 3
    valid_choice = False
    while not valid_choice:
        filename = input("What is the name of the file\n")
        if os.path.exists(filename):
            # it is open in read where the list of names is appended to a list where you can choose if you want to add new names or see the info of the names again this also has validation
            datafile = open(filename, "r")
            for names in datafile:
                x = names[:-1]
                list_of_names.append(x)
            print("Press 1 if you want to see the information of the names in your file")
            print("Press 2 if you want add more names to your list")
            user_choice = input("Which number do you choose\n")
            if user_choice == "1":
                valid_choice = True
                what_the_user_wants_to_do_with_list_of_names(list_of_names)
            elif user_choice == "2":
                valid_choice = True
                where_the_user_types_names(list_of_names)
            else:
                print("Invalid choice")
        elif tries == 1:
            valid_choice = True
            main_menu()
        elif not os.path.exists(filename):
            tries = tries - 1
            print("This file does not exist and you only have",
                  tries, "tries before you are taken to the menu")


def where_the_user_types_names(list_of_names):
    # if the user wants to create a new list of names, we ask the user to type a valid name which is appended ti a list only if it a valid
    user_input = ""
    while user_input != "information":
        user_input = input(
            "Enter a name or type 'information' to see the info your names or type 'main_menu' to go to the main menu\n")
        if user_input == "information":
            what_the_user_wants_to_do_with_list_of_names(list_of_names)
        elif user_input == "main menu":
            main_menu()
        elif user_input.isalpha():
            user_input = user_input.lower()
            list_of_names.append(user_input)
        else:
            print("Names dont have numbers or special charecters")


def main_menu():
    # its the main menu so i ask the user if they want to create a new list of names or load a list of names or quit the program and again there is validation
    list_of_names = []
    valid_user_choice = False
    while not valid_user_choice:
        print("Press 1 if you want to create a new list of names and save it into a file")
        print("Press 2 if you want to load a new list of names")
        print("Press 3 if you want to quit the program")
        user_choice = input("Which number do you choose\n")
        if user_choice == "1":
            where_the_user_types_names(list_of_names)
        elif user_choice == "2":
            get_names_from_users_file(list_of_names)

        elif user_choice == "3":
            print("Good bye")
            exit()
        else:
            print("Invalid choice")


main_menu()
