import random


def user_and_comp_choice():

    comp_choice = random.randint(1, 3)
    print("Press 1 if you choose Rock")
    print("Press 2 if you choose Paper")
    print("Press 3 if you choose Scissors")
    user_choice = input("Which number do you choose ?\n")
    return user_choice, comp_choice


def comp_choice_is_rock(player_choice, player_score, comp_score):

    if player_choice == "1":
        print("You chose Rock ")
        print("Computer chose Rock")
        print("Its a tie")
        player_score += 0
        comp_score += 0
        print("Player score:", player_score)
        print("Computer score:", comp_score)
        return player_score, comp_score

    elif player_choice == "2":
        print("You chose Paper")
        print("Computer chose Rock")
        print("Player wins")
        player_score += 1
        comp_score += 0
        print("Player score:", player_score)
        print("Computer score:", comp_score)
        return player_score, comp_score

    elif player_choice == "3":
        print("You chose Scissors")
        print("Computer chose Rock")
        print("Computer wins")
        player_score += 0
        comp_score += 1
        print("Player score:", player_score)
        print("Computer score:", comp_score)
        return player_score, comp_score


def comp_choice_is_paper(player_choice, player_score, comp_score):

    if player_choice == "1":
        print("You chose Rock ")
        print("Computer chose Paper")
        print("Computer wins")
        player_score += 0
        comp_score += 1
        print("Player score:", player_score)
        print("Computer score:", comp_score)
        return player_score, comp_score

    elif player_choice == "2":
        print("You chose Paper")
        print("Computer chose Paper")
        print("Its a tie")
        player_score += 0
        comp_score += 0
        print("Player score:", player_score)
        print("Computer score:", comp_score)
        return player_score, comp_score

    elif player_choice == "3":
        print("You chose Scissors")
        print("Computer chose Paper")
        print("Player wins")
        player_score += 1
        comp_score += 0
        print("Player score:", player_score)
        print("Computer score:", comp_score)
        return player_score, comp_score


def comp_choice_is_scissors(player_choice, player_score, comp_score):

    if player_choice == "1":
        print("You chose Rock ")
        print("Computer chose Scissors")
        print("Player wins")
        player_score += 1
        comp_score += 0
        print("Player score:", player_score)
        print("Computer score:", comp_score)
        return player_score, comp_score

    elif player_choice == "2":
        print("You chose Paper")
        print("Computer chose Scissors")
        print("Computer wins")
        player_score += 0
        comp_score += 1
        print("Player score:", player_score)
        print("Computer score:", comp_score)
        return player_score, comp_score

    elif player_choice == "3":
        print("You chose Scissors")
        print("Computer chose Scissors")
        print("Its a tie")
        player_score += 0
        comp_score += 0
        print("Player score:", player_score)
        print("Computer score:", comp_score)
        return player_score, comp_score


def where_the_game_is_executed(player_score, comp_score):

    valid_user_choice = False
    while not valid_user_choice:
        user_choice, comp_choice = user_and_comp_choice()

        if not user_choice.isnumeric():
            print("Invalid choice")
        elif int(user_choice) < 1 or int(user_choice) > 3:
            print("Invalid choice")
        else:
            valid_user_choice = True

            if comp_choice == 1:

                player_score, comp_score = comp_choice_is_rock(
                    user_choice, player_score, comp_score)

                if player_score == 10:
                    print("Player wins\n")
                    valid_choice = False
                    while not valid_choice:
                        ask = input(
                            "Do you want to play again, yes for'y' and no for'n'\n ")
                        if ask == "y":
                            valid_choice = True
                            where_the_game_is_executed(0, 0)
                        elif ask == "n":
                            valid_choice = True
                            print("\nGood bye")
                            exit()
                        else:
                            print("Invalid user choice")

                elif comp_score == 10:
                    print("Computer wins")
                    valid_choice = False
                    while not valid_choice:
                        ask = input(
                            "Do you want to play again, yes for'y' and no for'n'\n ")
                        if ask == "y":
                            valid_choice = True
                            where_the_game_is_executed(0, 0)
                        elif ask == "n":
                            valid_choice = True
                            print("\nGood bye")
                            exit()
                        else:
                            print("Invalid user choice")

                else:
                    where_the_game_is_executed(player_score, comp_score)

            elif comp_choice == 2:

                player_score, comp_score = comp_choice_is_paper(
                    user_choice, player_score, comp_score)
                if player_score == 10:
                    print("Player wins")
                    valid_choice = False
                    while not valid_choice:
                        ask = input(
                            "Do you want to play again, yes for'y' and no for'n'\n ")
                        if ask == "y":
                            valid_choice = True
                            where_the_game_is_executed(0, 0)
                        elif ask == "n":
                            valid_choice = True
                            print("\nGood bye")
                            exit()
                        else:
                            print("Invalid user choice")

                elif comp_score == 10:
                    print("Computer wins")
                    valid_choice = False
                    while not valid_choice:
                        ask = input(
                            "Do you want to play again, yes for'y' and no for'n'\n ")
                        if ask == "y":
                            valid_choice = True
                            where_the_game_is_executed(0, 0)
                        elif ask == "n":
                            valid_choice = True
                            print("\nGood bye")
                            exit()
                        else:
                            print("Invalid user choice")

                else:
                    where_the_game_is_executed(player_score, comp_score)

            elif comp_choice == 3:

                player_score, comp_score = comp_choice_is_scissors(
                    user_choice, player_score, comp_score)
                if player_score == 10:
                    print("Player wins")
                    valid_choice = False
                    while not valid_choice:
                        ask = input(
                            "Do you want to play again, yes for'y' and no for'n'\n ")
                        if ask == "y":
                            valid_choice = True
                            where_the_game_is_executed(0, 0)
                        elif ask == "n":
                            valid_choice = True
                            print("\nGood bye")
                            exit()
                        else:
                            print("Invalid user choice")

                elif comp_score == 10:
                    print("Computer wins")
                    valid_choice = False
                    while not valid_choice:
                        ask = input(
                            "Do you want to play again, yes for'y' and no for'n'\n ")
                        if ask == "y":
                            valid_choice = True
                            where_the_game_is_executed(0, 0)
                        elif ask == "n":
                            valid_choice = True
                            print("\nGood bye")
                            exit()
                        else:
                            print("Invalid user choice")

                else:
                    where_the_game_is_executed(player_score, comp_score)


where_the_game_is_executed(0, 0)
