
# the line isHappyNumber() will tell whether a number you inputed  is happy or not
def ishappynumber(number):
    rem = sum = 0

    # Calculates the sum of squares of digits
    while(number > 0):

        rem = number % 10

        sum = sum + (rem*rem)

        number = number // 10
# the return statement means that the new value of sum  is returned/ replaced the old value of sum
    return sum


# this is an input statement
number = int(input(
    "type in the number you want to find if it is happy number or sad number\n"))
# the value of result  is equal to value of number
result = number
# the while statement  would keep looping until result is equal to 1 and equal to 4
while(result != 1 and result != 4):

    result = ishappynumber(result)

# this would take the value of result from the while loop check if result is equal to 1 and print "is a happy number" if it doesnt meet the statement  it will then check the elif statement and if it does meet the elif statement it will print"not a happy number
if(result == 1):

    print(number, "is a happy number!!!")


# Unhappy number ends in a cycle of repeating numbers which contain 4
elif(result == 4):

    print(number, "is not a happy number!!!")
