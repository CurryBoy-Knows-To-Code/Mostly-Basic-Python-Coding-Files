def number_validation():
    # we assign the boolean 'False' to the variable 'validcheck'
    validcheck = False
    # this is a while loop to validate the user input
    while not validcheck:
        # this is a input statement stored in the variable 'number'
        number = input(
            "Enter the number to tell whether the number is strong or not\n")
        # the if statement checks if the input is a number and if it is true it will change the boolean of 'validcheck' to 'true' calculating the input if it is a strong number or not and stoping the while loop
        if str(number).isnumeric():
            validcheck = True
            # value of number is also stored in the variable 'temporary_number' which is only gonna be used in the while and for loop and we change the input which is a string to a integer
            return int(number)
        else:
            print("\ninvalid input it should be a positive number pls try again\n")
        # if this while loop is true this while loop executes the tabulated line below tilll line 20 if the variable 'temporary_number' is greater than 0


def strong_number_check():
    sum1 = 0
    temporary_number = number_validation()
    strnum = temporary_number

    while temporary_number > int(0):
        fact = 1
# this line calculates the reminder of the inputed number to find the individual factorial of the number
        reminder = temporary_number % 10
    # this for loop starts at 1 but end at the value of reminder of the calculated reminder also 1 is added to thr reminder and a new value of fact is calculated every time this for loop is executed
        for x in range(1, reminder + 1):
            fact = fact * x
    # the new value sum1 is calculated because the value of fact is added to sum1
        sum1 = sum1 + fact
    # this line does finds the quotient of the inputed number
        temporary_number = temporary_number // 10
    # if the input is not a positive number it will ask the user again and again until the input is a positive number
# because we calculated the factorials of the inputed number stored in the variable sum 1 it will be compared to the original inputed number and prints weather a number is strong or not a strong number
    if sum1 == int(strnum):
        print(strnum, "is a Strong Number!!!")
    else:
        print(strnum, "is not a Strong Number!!!")


strong_number_check()
