def user_input_and_validation():
    validation_check = False
    while not validation_check:
        day = input("What is the day ?\n")
        format = input(
            "What format do you want your number to be represented in ?\n")
        if not day.isdigit():
            print("Day is not a number")
        elif int(day) < 1 or int(day) > 7:
            print("Day must be between 1 and 7")

        elif format == "day" or format == "shortday" or format == "char":
            validation_check = True
            return day, format
        else:
            print("You can only choose 3 tupes of formats : day, shortday,char")


def day_format(day):
    if day == "1":
        print("Monday")
    elif day == "2":
        print("Tuesday")
    elif day == "3":
        print("Wednesday")
    elif day == "4":
        print("Thursday")
    elif day == "5":
        print("Friday")
    elif day == "6":
        print("Saturday")
    elif day == "7":
        print("Sunday")


def shortday_format(day):
    if day == "1":
        print("Mon")
    elif day == "2":
        print("Tue")
    elif day == "3":
        print("Wed")
    elif day == "4":
        print("Thu")
    elif day == "5":
        print("Fri")
    elif day == "6":
        print("Sat")
    elif day == "7":
        print("Sun")


def char_format(day):
    if day == "1":
        print("M")
    elif day == "2":
        print("Tu")
    elif day == "3":
        print("W")
    elif day == "4":
        print("Th")
    elif day == "5":
        print("F")
    elif day == "6":
        print("Sa")
    elif day == "7":
        print("Su")


def chosen_format():
    day, format = user_input_and_validation()

    if format == "day":
        day_format(day)

    elif format == "shortday":
        shortday_format(day)

    elif format == "char":
        char_format(day)


chosen_format()
