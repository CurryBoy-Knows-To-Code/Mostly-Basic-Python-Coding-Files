import random


def does_player_want_to_play_again_choice():
    # after guessing the the correct number your are asked whether you want to play again
    #  it validates your input
    valid = False
    while not valid:
        print("\nPress 1 to play again, you will be taken back to the menu")
        print("Press 2 if you want to exit the game")
        choice = input("which number do you choose\n")
        if not str(choice).isnumeric() or int(choice) < 1 or int(choice) > 2:
            print("Invalid choice")
        elif choice == "1":
            user_choice_mode()
        elif choice == "2":
            print("Good bye")
            exit()


def user_choice_validation_for_easy_and_normal_mode():
    # in easy and normal mode you guess a 4 digit number and it validates it whether it is a number and it is 4 digits
    valid = False
    while not valid:
        number_choice = input("Guess the 4 digit number:")
        if not number_choice.isnumeric():
            print("Invalid choice")
        elif int(number_choice) < 1000 or int(number_choice) > 9999:
            print("Invalid choice")
        else:
            return str(number_choice)


def user_choice_is_valid_for_hard_mode():
    # in hard mode you guess a 5 digit number and validates it corresponding to its digits
    valid = False
    while not valid:
        number_choice = input("Guess the 5 digit number:")
        if not number_choice.isnumeric():
            print("Invalid choice")
        elif int(number_choice) < 10000 or int(number_choice) > 99999:
            print("Invalid choice")
        else:
            return str(number_choice)


def easy_mode():
    # in easy mode you show how may digits it got correct
    computer_number = str(random.randint(1000, 9999))
    # gets the input and check if you guessed in first try
    user_number = user_choice_validation_for_easy_and_normal_mode()
    if (user_number == computer_number):
        print("You guessed the number correctly")
        does_player_want_to_play_again_choice()
    else:
        # if it is not the correct number we use a while loop till you enter the correct number

        while (user_number != computer_number):

            count = 0
            # ["X"] * 4 basically ["X","X","X","X"]
            correct = ['X'] * 4
            # we use a for loop to see if the inputs index matches the computers number index value
            for x in range(0, 4):
                # if the index of both match it will replace the correct index ["X","X","X","X"] with the number which is show to the user
                if (user_number[x] == computer_number[x]):
                    count += 1
                    correct[x] = user_number[x]
                else:
                    continue
            if (count < 4) and (count != 0):

                print("incorrect number. But you did get ",
                      count, " digit(s) correct!")
                print("Also these numbers in your input were correct.")
                # this for prints out the list of correct numbers you guessed
                for i in correct:
                    print(i, end=' ')
                print('\n')
                print('\n')
                user_number = user_choice_validation_for_easy_and_normal_mode()
            elif (count == 0):
                print("None of the numbers in your input match.")
                user_number = user_choice_validation_for_easy_and_normal_mode()
        if user_number == computer_number:
            print("you finally guessed it correctly")
            does_player_want_to_play_again_choice()


def normal_mode():
    # same thing happens as easy mode but you dont show the correct guessed numbers
    computer_number = str(random.randint(1000, 9999))
    user_number = user_choice_validation_for_easy_and_normal_mode()
    if (user_number == computer_number):
        print("You guessed the number correctly")
        does_player_want_to_play_again_choice()
    else:
        while (user_number != computer_number):
            count = 0
            for x in range(0, 4):
                if (user_number[x] == computer_number[x]):
                    count += 1
                else:
                    continue
            if (count < 4) and (count != 0):
                print("incorrect number. But you did get ",
                      count, " digit(s) correct!")
                user_number = user_choice_validation_for_easy_and_normal_mode()
            elif (count == 0):
                print("None of the numbers in your input match.")
                user_number = user_choice_validation_for_easy_and_normal_mode()
        if user_number == computer_number:
            print("you finally guessed it correctly")
            does_player_want_to_play_again_choice()


def hard_mode():
    # same thing happens in normal mode but it is a 5 digit number so for loops start at 5  basically what was 4 now is 5
    computer_number = str(random.randint(10000, 99999))
    user_number = user_choice_is_valid_for_hard_mode()
    if (user_number == computer_number):
        print("You guessed the number correctly")
        does_player_want_to_play_again_choice()
    else:
        while (user_number != computer_number):
            count = 0
            for x in range(0, 5):
                if (user_number[x] == computer_number[x]):
                    count += 1
                else:
                    continue
            if (count < 5) and (count != 0):
                print("incorrect number. But you did get ",
                      count, " digit(s) correct!")
                user_number = user_choice_is_valid_for_hard_mode()
            elif (count == 0):
                print("None of the numbers in your input match.")
                user_number = user_choice_is_valid_for_hard_mode()
        if user_number == computer_number:
            print("you finally guessed it correctly")
            does_player_want_to_play_again_choice()


def user_choice_mode():
    # this is the function where the user gets to choose if the want to guess the number in easy, normal, hard mode and it validates the input so that the input is not out of bounds or a word
    validation = False
    while not validation:
        print("Press 1 if you choose easy mode")
        print("Press 2 if you choose normal mode")
        print("Press 3 if you choose hard mode")
        print("press 4 if you choose to leave the game")
        user_choice = input("which number do you choose\n")
        # calls a specific function depending on which diffulty you choose
        if not str(user_choice).isnumeric() or int(user_choice) < 1 or int(user_choice) > 4:
            print("Invalid choice")
        elif user_choice == "1":
            validation = True
            easy_mode()
        elif user_choice == "2":
            validation = True
            normal_mode()
        elif user_choice == "3":
            validation = True
            hard_mode()
        elif user_choice == "4":
            print("Good bye")
            exit()


user_choice_mode()
