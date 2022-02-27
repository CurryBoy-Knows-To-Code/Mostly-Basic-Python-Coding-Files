# validation for P1 input
def player_1_input():
    valid_for_p1 = False
    while not valid_for_p1:
        p1 = input("enter your number player 1\n")
        # checks if it is numeroc and between 1 and 3 inclusive
        if not p1.isnumeric():
            print("Only enter a number")
        elif int(p1) < 1 or int(p1) > 3:
            print("input should be between 1 and 3")
        else:
            print("valid input")
            valid_for_p1 = True
            return int(p1)

# same validation but for P2 input


def player_2_input():
    valid_for_p2 = False
    while not valid_for_p2:
        p2 = input("enter your number player 2\n")
        if not p2.isnumeric():
            print("Only enter a number")
        elif int(p2) < 1 or int(p2) > 3:
            print("input should be between 1 and 3")
        else:
            print("valid input")
            valid_for_p2 = True
            return int(p2)


def game_executer():
    # the total amount of sticks is 27
    sticks = 27
    while sticks >= 1:
        # we are getting P1 input
        p1_choice = player_1_input()
        # after P1 input you get new value of sticks which is shown in the terminal
        sticks = sticks - p1_choice
        print(sticks, "sticks remaining")
        # checks if the sticks are less than or equal to 0 and if it is then it asks both users whether the want to play again
        if sticks <= 0:
            print("you lose Player 1")
            validation = False
            while not validation:
                user_choice_p1 = input(
                    "do you want to play again player 1,yes or no\n")
                user_choice_p2 = input(
                    "do you want to play again player 2,yes or no\n")
                if user_choice_p1 == "yes" and user_choice_p2 == "yes":
                    game_executer()
                elif user_choice_p1 == "no" or user_choice_p2 == "no":
                    print("good bye")
                    exit()
                else:
                    print("invalid input, either type yes or no")
        # but if the sticks are are greater than 0
        # P2 will get to reduce the amount of sticks
        # again it will check if sticks are less than equal to 0 and then ask if they want to pay again
        p2_choice = player_2_input()
        sticks = sticks - p2_choice
        print(sticks, "sticks remaining")
        if sticks <= 0:
            print("you lose Player 2")
            validation = False
            while not validation:
                user_choice_p1 = input(
                    "do you want to play again player 1,yes or no\n")
                user_choice_p2 = input(
                    "do you want to play again player 2,yes or no\n")
                if user_choice_p1 == "yes" and user_choice_p2 == "yes":
                    game_executer()
                elif user_choice_p1 == "no" or user_choice_p2 == "no":
                    print("good bye")
                    exit()
                else:
                    print("invalid input, either type yes or no")


game_executer()
