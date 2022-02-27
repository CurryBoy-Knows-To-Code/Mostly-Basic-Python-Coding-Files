# this an input statement where you type in your number
num = float(input("type in your number\n"))


def state_check(number):
    # this is a condition where if the input is smaller 1 it prints solid
    if number < 1:
        print(" it is a solid")
    # this is a condition where if the input is between 1-99 it prints liquid
    elif number >= 1 and number <= 99:
        print("it is a liquid")
    # if the input does not meet the condition of the if and elif statements it prints gas
    else:
        print("it is a gas ")


state_check(num)
