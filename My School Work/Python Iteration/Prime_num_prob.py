def prime_num_check(number):
    # if the input is greater than 1 it will carry out the tasks under tabed parts  until line 11
    if number == 1:
        return str(number)+" is not a prime number"
    elif number > 1:
        # the range starts at 2 and ends at the number you have inputed
        for i in range(2, number):
            # if input / i  remainder = 0 ,print   not prime number
            if (number % i) == 0:
                return str(number)+" is not a prime number"
    #  The break statement  terminates the current loop and resumes execution at the next statement
                break

    # if it does not meet the statement above it will print is prime number
        else:
            return str(number)+" is a prime number"


####### Main program #######
# this is an input statement
num = int(input("Enter a number: "))
output = prime_num_check(num)
print("{}".format(output))
