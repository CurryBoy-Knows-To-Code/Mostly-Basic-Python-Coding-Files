def user_input():

    pounds = float(input("How many pounds do you have ?\n"))
    print("the input should be in caps")
    print("USD or EURO or YUAN or YEN")
    currency = input("Which currency would you like to convert it to ?\n")
    return pounds, currency


def exchange_rate():

    pounds, currency = user_input()

    if currency == "USD":
        USD = 1.39 * pounds
        print("£", pounds, "is", USD, "dollars")
    elif currency == "EURO":
        EURO = 1.18 * pounds
        print("£", pounds, "is", round(EURO, 2), "euros")

    elif currency == "YUAN":
        YUAN = 9.13 * pounds
        print("£", pounds, "is", round(YUAN, 2), "yuan")
    elif currency == "YEN":
        YEN = 153.18 * pounds
        print("£", pounds, "is", round(YEN, 2), "yen")


exchange_rate()
