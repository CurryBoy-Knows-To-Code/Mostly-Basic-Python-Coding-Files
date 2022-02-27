# we use statistics so that we can fing the mean median mode easily
import statistics


def user_input_validation():
    # we validate the input to make sure it is a float and not a string
    # we use a try and except because when trying to convert the input to a float when the input is a word it raises a ValueError
    # if the input is valid then we append it to a list and keep asking the input ultil ther user wants to find information about the list of numbers

    try:
        list_of_numbers = []
        user_input = ""
        while user_input != "data":
            user_input = input(
                "Enter your number or type data to find information about your numbers\n")
            if user_input == "data":
                return str(user_input), list_of_numbers
            elif float(user_input) < 0:
                user_input = float(user_input)
                list_of_numbers.append(user_input)
            elif user_input.isnumeric():
                user_input = float(user_input)
                list_of_numbers.append(user_input)
    except ValueError:
        print("Invalid number")
        meaning_of_user_numbers()


def add_list_of_numbers_and_data_of_numbers(list_of_numbers, mean, median, mode):
    # if you did choose to save the list of numbers it will open the file in write mode  and add the list of numbers and its information and after that you get to choose if you want see the file or add new list of numbers or quit the program
    # again there is also validation to the input
    filename = "user list of numbers and meaning"
    datafile = open(filename, "a")
    datafile.write("\nUser list of numbers: {}\n".format(list_of_numbers))
    datafile.write("Mean for list of numbers: {}\n".format(mean))
    datafile.write("Median for list of numbers: {}\n".format(median))
    datafile.write("Mode for list of numbers: {}\n".format(mode))
    datafile.close()
    valid_and_choice = False
    while not valid_and_choice:
        print("Press 1 if you want to see the list of numbers and their meaning")
        print("Press 2 if you want to add a new list of numbers")
        print("Press 3 if you want to quit")
        user_choice = input("Which number do you choose\n")
        if user_choice == "1":
            datafile = open(filename, "r")
            print(datafile.read())
            valid_and_choice = True
        elif user_choice == "2":
            valid_and_choice = True
            meaning_of_user_numbers()
        elif user_choice == "3":
            print("Good bye")
            exit()
        else:
            print("Invalid choice")


def meaning_of_user_numbers():
    user_input, list_of_numbers = user_input_validation()
    # if the user wants to find info of the list of numbers but there is no numbers then it will ask to type the list of numbers

    if len(list_of_numbers) > 0:
        # finds mean median mode of numbers and prints out then asks the user if they want save the list of numbers and its information
        # this also has validation
        mean = statistics.mean(list_of_numbers)
        median = statistics.median(list_of_numbers)
        mode = statistics.mode(list_of_numbers)
        print("the average of the entered numbers is", mean)
        print("the median of the entered numbers is", median)
        print("The mode of the entered numbers is", mode)
        valid_and_choice = False
        while not valid_and_choice:
            print("Press 1 to save list of numbers and data of numbers")
            print("Press 2 to exit  ")
            user_choice = input("Which number do you choose\n")
            if user_choice == "1":
                add_list_of_numbers_and_data_of_numbers(
                    list_of_numbers, mean, median, mode)
                valid_and_choice = True
            elif user_choice == "2":
                print("Good bye")
                exit()
            else:
                print("invalid choice")
    else:
        # Mr Challice did this print line
        print("Ha ha, show me the numbers!")
        meaning_of_user_numbers()


meaning_of_user_numbers()
