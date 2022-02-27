def times_table_program():

    user_input = float(input("Enter number\n"))
    what_number = int(
        input("Till what number do you want to multiply it with\n"))
    # we use for loop to start from 1 all the way up to what number you chose such as up to 20
    for num in range(1, what_number + 1):
        print(user_input, "x", num, "=", user_input * num)
    user_menu()


def square_numbers_problem():
    # same principle as  times table program but we do ** 2 which is  user input to the power of 2
    user_input = int(input("Enter your number\n"))
    for num in range(1, user_input + 1):
        print(num, "squared is", num ** 2)


def user_menu():
    # here you can choose if you want to do times table or square numbers and as usual there is validation
    valid_input = False
    while not valid_input:
        print("Press 1 if you want to use the times table program")
        print("Press 2 if you want to use the square numbers program")
        user_input = input("Which number do you choose\n")
        if user_input == "1":
            times_table_program()
        elif user_input == "2":
            square_numbers_problem()
            pass
        else:
            print("Invalid input")


user_menu()
