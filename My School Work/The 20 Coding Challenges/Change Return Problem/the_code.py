import random


def change_calculator(currency, dev_test):
    # we use a try and except because if the user types an letter or special charecter rather than a number we try to float  it which doesnt work so it will raise a ValueError to catch that we use the try and except
    try:
        dev_check_value = 0
        valid_inputs = False
        while not valid_inputs:

            if dev_test == "yes":
                # we generate a random number but it has to be a floating point as well so we use the random.uniform function but it will create more than 2 decimal places do we round of the number using the rounf fucntion round(number,number of places)
                total_cost = round(random.uniform(24, 2544), 2)
                amount_paid = round(random.uniform(total_cost, 3000), 2)
                print(total_cost)
                print(amount_paid)
            elif dev_test == "no":
                total_cost = round(float(input("What is the total cost\n")), 2)
                amount_paid = round(
                    float(input("How much are you gonna pay\n")), 2)
            if amount_paid == total_cost:
                valid_inputs = True
                print("0 change")
                main_menu()
            elif amount_paid > total_cost:
                valid_inputs = True
                # here we calculate the change but sometimes the decimal places are also more than 2 so we round this off as well
                change = round(amount_paid - total_cost, 2)
                print("The change you should get is", change)
                check_change = change
                # we are looping through the dictionary but there are 2 values you can get which is the key and the value paired with it
                # the currency.items(), gets the key which is stored in the variable denomination and then its value which is stored in the variable value
                for denomination, value in currency.items():
                    # this keeps track of how many times the first value can be divided by the change
                    count = int(change/value)

                    change = round(change % value, 2)
                    dev_check_value += (value * count)
                    print("Number of", denomination, "to return is", count)
                # the multiple if statements you see basically tells whether the denominations of the program actually to the actual change
                if dev_test == "yes":
                    dev_check_value = round(dev_check_value, 2)
                    if dev_check_value == check_change:
                        print("the change you should get is", check_change)
                        print(" the change adds up to", dev_check_value)
                        print(
                            "The denomination adds up to the change so the program works")
                        main_menu()
                    elif dev_check_value != check_change:
                        print("the change you should get is", check_change)
                        print(" the change adds up to", dev_check_value)
                        print("They dont add upp there must be some problem")
                        main_menu()
                if dev_test == "no":
                    main_menu()
            else:
                print("amount paid cant be lower than the total cost")
    except ValueError:
        print("Only numbers are allowed")
        change_calculator(currency)


def main_menu():
    # this the main menu where you get to choose which currency you want to choose test whether the change output is correct
    # there is validation for this
   # under this line is a dictionary which has a key and value with it for example the key "£100" has a value  100 this is shown as {"£100":100}
    # basically a dictionary is a list where you can add, delete variables which must have a value
    uk_denominations = {
        "£50": 50.00, "£20": 20.00, "£10": 10.00,
        "£5": 5.00, "£2": 2.00, "£1": 1.00,
        "50p": 0.50, "20p": 0.20, "10p": 0.10,
        "5p": 0.05, "2p": 0.02, "1p": 0.01}

    usa_denominations = {
        "$100": 100.00, "$50": 50.00, "$20": 20.00,
        "$10": 10.00, "$5": 5.00, "$2": 2.00,
        "$1": 1.00, "50 cents": 0.50, "quater": 0.25,
        "dime": 0.10, "nickel": 0.05, "penny": 0.01}

    valid_choice = False
    while not valid_choice:
        print("Press 1 if you want to use pound(£) denominatins")
        print("Press 2 if you want to dollars($) denominations")
        print("Press 3 for testing the change")
        user_choice = input("Which number do you choose\n")
        if user_choice == "1":
            valid_choice = True
            # under this line is a dictionary which has a key and value with it for example the key "£100" has a value  100 this is shown as {"£100":100}
            # basically a dictionary is a list where you can add, delete variables which must have a value

            change_calculator(uk_denominations, "no")
        elif user_choice == "2":
            valid_choice = True

            change_calculator(usa_denominations, "no")
        elif user_choice == "3":
            valid_choice = True
            choice = random.randint(1, 2)
            print(choice)
            if choice == 1:

                change_calculator(uk_denominations, "yes")
            elif choice == 2:
                change_calculator(usa_denominations, "yes")
        else:
            print("Invalid choice")


main_menu()
