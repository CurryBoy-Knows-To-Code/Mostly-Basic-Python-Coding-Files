def pin_validation():
    # PIN is false.
    PIN = True
# the value 0 is assigned to the variable 'count'.
    count = 0
# this is where you type your initial PIN number
    pin1 = int(input("Enter your new PIN number\n"))
    print("")
# while not PIN means while PIN is false execute the tabulated lines below till line 19
    while PIN:
        # this input statement is asked for verification
        vpin = int(input("Enter your PIN number again for verification\n"))
        # if the first input is equal to the verfication input  it will stop looping because we are changing PIN from False to True and it will print("Hello")
        if pin1 == vpin:
            PIN = False
            print("Hello")
        # but if the first input statement is not equal to the verification input it will ask again for the verification input again because we have not changed PIN to true and it will ask us to type it again and 1 is added to the variable count
        elif pin1 != vpin:
            print("Invalid PIN. Try again.")
            print("")
            count = count+1
        # because 1 is added to count when you type your pin wrong this statement will execute only if count is equal to 3 and your initial pin is not equal ti the verificatin pin  the loop would stop because we change PIN from False to True
        if count == 3 and pin1 != vpin:
            PIN = False
            print("locked out")


pin_validation()
