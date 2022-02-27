import os
# json basically changes string to list,tuples,dictionaries etc and vice versa
import json


def user_input_validation(users_input):
    # are input validation
    # we use a try and except because when conveting a string to a float the input could be letters which will raise a ValueError
    try:
        users_input = float(users_input)
        if type(users_input) == float:
            return True, users_input

    except ValueError:
        return False, users_input


def get_info_from_users_file(list_of_numbers):
    # this is where we get the contents from the users file
    information_list = []
    # you only have 3 tries to type in the correct file name
    tries = 0
    valid_file_name = False
    while not valid_file_name:
        filename = input("What is the name of file\n")
        # check if the file exists or not
        if os.path.exists(filename) == True:
            valid_file_name = True
            # i open the file in read mode then we use a for loop to write each line to the variable information while we use strip
            datafile = open(filename, "r")
            for information in datafile:
                information_list.append(information.strip())
            # we use the replace fuction to remove the unnecessary details and replacing it with a empty string this works for numbers and letters but not lists
            numbers = information_list[0].replace("List of numbers are: ", "")
            # in the variable the whole list is a sting example "[2,4,3,4,5,4,5]" so using a for loop to append the numbers only doesnt work
            # we use json by using the loads function to change that string list to a normal usable list, this also works if your string is like a dictionary or 2D list or tuple and etc
            list_of_numbers = json.loads(numbers)
            maximum_bound = information_list[1].replace(
                "Maximum bound is: ", "")
            minimum_bound = information_list[2].replace(
                "Minimum bound is: ", "")
            valid_choice = False
            while not valid_choice:
                # ask user whether he wants to use the same bounds asthe contents of the file or if he wants to change them

                print("Press 1 if you want use the same bounds which is numbers between",
                      minimum_bound, "and", maximum_bound, "both inclusive")
                print("Press 2 if you want to change your bounds")
                user_choice = input("Which number do you choose\n")
                if user_choice == "1":
                    # validation
                    max_and_min_calculator(
                        maximum_bound, minimum_bound, list_of_numbers)
                elif user_choice == "2":
                    get_max_and_min_bounds(list_of_numbers)
                else:
                    print("Invalid choice")
        elif tries == 2:
            valid_file_name = True
            print("Sorry but we are taking you back to the main menu")
            user_menu()
        else:
            tries += 1
            print("The file you tried to open does not exist")


def save_users_list_and_its_info(list_of_numbers, maximum_bound, minimum_bound):

    maximum_value = max(list_of_numbers)
    minimum_value = min(list_of_numbers)
    file_name_exists = True
    while file_name_exists:
        file_name = input("What would you like to name your file\n")
        # importing os to see if the file exists already beacuse if it does we ask the  user to save it ina different file name
        if os.path.exists(file_name) == True:
            print("Choose a different file name")
        elif os.path.exists(file_name) == False:
            file_name_exists = False
            # so the file name doesnt exist so we open the file name in write mode
            datafile = open(file_name, "w")
            # we write its contents and then we close it
            # we use format because you cant use + or , to write multiple variables in the file
            datafile.write("List of numbers are: {}".format(list_of_numbers))
            datafile.write("\nMaximum bound is: {}\n".format(maximum_bound))
            datafile.write("Minimum bound is: {}\n".format(minimum_bound))
            datafile.write("Maximum value is: {}\n".format(maximum_value))
            datafile.write("Minimum value is: {}\n".format(minimum_value))
            datafile.close()
            print("List of numbers and its information has been written to the file")

            user_menu()

# this is our main function with 3 args which very important


def max_and_min_calculator(users_maximum_bound, users_minimum_bound, list_of_numbers):
    # we our bounds and list of numbers
    user_input = ""
    # we a while loop so that it keeps asking the user the input unless they type 'main menu' or 'save to a file'
    while user_input != "main menu" or user_input != "save to a file":
        # shows the min and max bounds all the time
        print("Maximum bound is:", users_maximum_bound, "inclusive")
        print("Minimum bound is:", users_minimum_bound, "inclusive")
        user_input = input(
            "Enter a number to find its max and min or type 'main menu' to go back to the main menu or type 'save to a file' to save it\n")
        if user_input == "main menu":
            user_menu()
            # we use a break statement so that it breaks out of the while loop
            break
        elif user_input == "save to a file":
            # len function is used to see whether the list is empty or not because if it is empty it means the user didnt type any number
            if len(list_of_numbers) == 0:
                print("There is no input")
            else:
                # we call the function where it saves the list of numbers and its info
                save_users_list_and_its_info(
                    list_of_numbers, users_maximum_bound, users_minimum_bound)
                break
        else:
            # validation of input
            valid_input, user_input = user_input_validation(user_input)
            if valid_input == True:
                # if it is valid then it will append the input to the list
                list_of_numbers.append(user_input)
                # in this for loop we are making a copy of 'list_of_numbers' using 'list_of_numbers[:]:'
                # this is because when removing items in a list under a for loop it messes up the index
                for number in list_of_numbers[:]:
                    # if the input is out of bounds or the user changed the bounds and the numbers existing in that list is outside that bound we remove it
                    if (number < float(users_minimum_bound)) or (number > float(users_maximum_bound)):
                        list_of_numbers.remove(number)
                # the reason we use a try and except is because if the list is empty and and the input is out of bounds it will try to print the max and min of a empty list which will raise an ValueError
                try:
                    print("List of numbers are:", list_of_numbers)
                    print("The maximum value is:", max(list_of_numbers))
                    print("The minimum value is:", min(list_of_numbers))
                except ValueError:
                    pass
            elif valid_input == False:
                print("Invalid input")


def get_max_and_min_bounds(list_of_numbers):
    # lots of validation as we call the function 'user_input_validation' while passing the what the minimum bound is then if that is valid we pass the next user input which is the maximum bound
    # and for each input you only have 3 tries and then you will be taken back to the main menu
    valid_minimum_bound = False
    valid_maximum_bound = False
    tries = 0
    while not valid_minimum_bound:
        users_minimum_bound = input("Enter your minimum_bound\n")
        valid_input, users_minimum_bound = user_input_validation(
            users_minimum_bound)
        if valid_input == True:
            tries = 0
            valid_minimum_bound = True
            while not valid_maximum_bound:
                users_maximum_bound = input("Enter your maximum bound\n")
                valid_input, users_maximum_bound = user_input_validation(
                    users_maximum_bound)
                if valid_input == True:
                    valid_maximum_bound = True
                    max_and_min_calculator(
                        users_maximum_bound, users_minimum_bound, list_of_numbers)
                elif tries == 2:
                    valid_minimum_bound = True
                    print("Sorry but we are taking you back to the main menu")
                    user_menu()
                elif valid_input == False:
                    tries += 1
                    print("Only enter a number")
        elif tries == 2:
            valid_minimum_bound = True
            print("Sorry but we are taking you back to the main menu")
            user_menu()
        elif valid_input == False:
            tries += 1
            print("Only enter a number")


def user_menu():
    # we ask what the user wants to do
    list_of_numbers = []
    valid_choice = False
    while not valid_choice:
        print(
            "Press 1 if you want to create a new list of numbers and find its max and min")
        print("Press 2 if you want to load a file with a list of numbers and its details")
        print("Press 3 if you want to quit the program")
        user_choice = input("Which number do you choose\n")
        if user_choice == "1":
            valid_choice = True
            # calls function to get maximum and minimum bounds and from ther it calls the main function to see max and min values in list
            get_max_and_min_bounds(list_of_numbers)
        elif user_choice == "2":
            # calls the function to load the users file
            get_info_from_users_file(list_of_numbers)
        elif user_choice == "3":
            print("Good bye")
            exit()
        else:
            print("Invalid choice")


user_menu()
