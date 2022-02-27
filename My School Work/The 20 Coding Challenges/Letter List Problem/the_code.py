import os


def find_letters_in_file(file_name):
    number_of_words_same_as_users_letter = 0
    valid_letter = False
    while not valid_letter:
        print("Press 1 if you want all the words starting with your chosen letter")
        print("Press 2 if you want all the words which has your chosen letters")
        users_choice = input("Which number do you choose\n")
        users_letter = input("Enter your letter\n")
        # we use validation so that the input is correct and
        if len(users_letter) == 1 and not users_letter.isnumeric() and users_choice.isnumeric():
            valid_letter = True
            datafile = open(file_name, "r")
            # we store each word in the file that the user has given but we have to use the split function to seperate words
            # storing it in one variable means that the words can be trated like a list
            letter_or_words = datafile.read().split()
            if users_choice == "1":
                # we use a for loop to go through each word in the list 'letter_or_words'
                for word in letter_or_words:
                    # in code, lists index start at 0 not 1 so the first letter in a word has a index of 0
                    if users_letter == word[0]:
                        print(word)
                        # just a neater way of adding
                        number_of_words_same_as_users_letter += 1
                print("Number of words that starts with letter", users_letter,
                      "in file", file_name, "is", number_of_words_same_as_users_letter)
            elif users_choice == "2":
                for word in letter_or_words:
                    # we check if the users letter is found anywhere in the word
                    if users_letter in word:
                        number_of_words_same_as_users_letter += 1
                        print(word)
                print("Number of words that has letter", users_letter, "in file",
                      file_name, "is", number_of_words_same_as_users_letter)
        else:
            print("One or both inputs are invalid")

# this is where we ask the user what is the file name and check wheether it exists or not


def does_user_file_exist():
    tries = 0
    existing_file = False
    while not existing_file:
        users_file = input(
            "Type in your letter list or list of words file name\n")
        # we import os so we could see whether the file exists
        if os.path.exists(users_file) == True:
            existing_file = True
            # we call the function 'find_letters_in_file' while passing the file name so that it can be opened to see the contents
            find_letters_in_file(users_file)
            # i have put a limit to the number of times you can type the correct file name
        elif tries == 9:
            existing_file = True
            print(
                "Because of many invalid attempts i am kicking you out of the program and also FUCK YOU !!!!")
            exit()
        elif os.path.exists(users_file) == False:
            tries += 1
            print("This file does not exist")


does_user_file_exist()
