import random


def get_random_word_from_file():
    # here we open a file which contains different words
    letters = []
    # we take the words and we split the strings by lines
    list_of_words_in_the_file = open(
        "list of random words.txt").read().splitlines()
    # here we randomly choose the word using random.choice
    random_word = random.choice(list_of_words_in_the_file)
    # we use a for loop to iterate through each letter in the word then we append it to the list letters
    for letter in random_word:
        letters.append(letter)
    return random_word, letters


def hangman_executer():
    users_random_word, users_random_word_as_a_list = get_random_word_from_file()
    # we use a single list which is multiplyed by the length of the word so example if the word was "boys" then we do ["_"] * 4 which will look like this ["_","_","_","_"]
    word_layout = ["─"] * len(users_random_word_as_a_list)
    # the list under is where we store the same letters
    guessed_letters = []
    valid_input = False
    while not valid_input:
        # we ask how many chances does the user want and this input is also validated
        no_of_chances = input("How many chances do you want to have\n")
        if no_of_chances.isnumeric() and int(no_of_chances) > 0 and int(no_of_chances) < 27:
            valid_input = True
            no_of_chances = int(no_of_chances)
            has_user_guessed_the_word = False
            print("Lets play Hangman")
            # here we use a while loop so that it keeps asking the user their guess until they guess it correctly or run out of tries
            while not has_user_guessed_the_word and no_of_chances > 0:
                print("You have", no_of_chances, "chances left")
                print(word_layout)
                users_guess = input("Guess the letter or word\n").lower()
                # here we check the length of the input because if it is a letter then then length will be one and the isalpha function checks if the input has a alphabet
                if len(users_guess) == 1 and users_guess.isalpha():
                    # here we check if they inputted the same letter
                    if users_guess in guessed_letters:
                        print("You already guessed this letter")
                    elif users_guess not in users_random_word_as_a_list:
                        # this elif statement checks if the input is in the word, if not then the chances decreases by 1 and then the input is appended so that the user doesnt loses its chnance if it does type the same word again
                        print("The letter you guessed in not in the word")
                        no_of_chances -= 1
                        guessed_letters.append(users_guess)
                        if no_of_chances == 0:
                            print("Sorry but you have run out of chances")
                            print("The word was", users_random_word)
                            has_user_guessed_the_word = True
                    else:
                        print("You guessed the correct letter")
                        guessed_letters.append(users_guess)
                        # here a for loop  is used as a index
                        for index in range(0, len(users_random_word_as_a_list)):
                            # we check if the index item is equal to the input if it is then we replace the index of the item of the word layout to the input then we continue again because if there was 2 or more of the same letter we have to replace it
                            if users_random_word_as_a_list[index] == users_guess:
                                word_layout[index] = users_guess
                            else:
                                continue
                        # the line under checks the items in the word list is same as the word layout and this is done by using the all function but if you want to check if one of the items are in both lists then we use the function any() and when using this it returns a boolean
                        check = all(
                            letter in users_random_word_as_a_list for letter in word_layout)
                        if check == True:
                            # if all the items in both lists exist then we  break the program
                            print("You guessed the word correctly")
                            print(users_random_word)
                            has_user_guessed_the_word = True
                        elif check == False:
                            pass
                elif len(users_guess) > 1 and users_guess.isalpha():
                    if users_guess == users_random_word:
                        print("You guessed the word correctly")
                        print(users_random_word)
                        no_of_chances -= 1
                        has_user_guessed_the_word = True
                else:
                    print("Not a valid guess")
        else:
            print("Invalid input")


hangman_executer()
