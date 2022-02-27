# this function gets the inputs from the user passes the inputs to the date validation function
def user_date_input():
    day = input("type in the day in the format dd \n")
    month = input("type in the month in the format mm \n")
    year = input("type in the year in the format yyyy \n")
    return day, month, year


# this function calculates if the year is a leapyear only if the date is valid
def leapyear_calc(year):
    if int(year) % 400 == 0 or int(year) % 4 == 0 and int(year) % 100 != 0:
        leapyear = "and its a leap year"
        return leapyear
    else:
        leapyear = ""
        return leapyear


def date_validation():
    # we assign the boolean to the variable'validation'
    validation = False
# this while loop is used to ask the user the date over and over until the input is correct
    while not validation:

        day, month, year = user_date_input()
        # this combines the inputs in form of dd/mm/yyyy
        format = (day+"/"+month+"/"+year)
        # this if statement checks if there is input for all the input statements
        if (len(day)) == 0 or (len(month)) == 0 or (len(year)) == 0:
            print("there is no input for one or more of the questions")
        # this elif statement checks the length of the input that there are 10 charecters in dd/mm/yyyy(including foward slashes)
        elif (len(day)) != 2 or (len(month)) != 2 or (len(year)) != 4 or (len(format)) != 10:
            print("number of charecters inputed is wrong")
        # this elif statement checks if the input is a number
        elif not day.isdigit() or not month.isdigit() or not year.isdigit():
            print("one or more of the inputs is not a number")
        # this elif statement checks if the day or month input is grater than 1 and the month is less than 12 and the year is greater than 1900
        elif int(day) < 1 or int(month) < 1 or int(month) > 12 or int(year) < 1900:
            print("day and month cannot be less than one and the month cannot be more than 12 and the year cannot be less than 1900")
        # if the month is 02 it will check that number of days does not exceed over 29 and if it doesn't it will change the boolean from False to True breaking the while loop
        elif month == "02":
            if int(day) > 29:
                print(month, "doesnt have days over 29")
            else:
                leapyear = leapyear_calc(year)
                validation = True
                print(format, "is a valid date", leapyear)
        # the same thing happens but just for the months which has 31 days
        elif month == "01" or month == "03" or month == "05" or month == "07" or month == "08" or month == "10" or month == "12":
            if int(day) > 31:
                print(month, "doesnt have days over 31")
            else:
                leapyear = leapyear_calc(year)
                validation = True
                print(format, "is a valid date", leapyear)
        # the same thing happens but just for the months which has 30 days
        elif month == "04" or month == "06" or month == "09" or month == "11":
            if int(day) > 30:
                print(month, "doesnt have days over 30")
            else:
                validation = True
                print(format, "is a valid date", leapyear)


date_validation()
