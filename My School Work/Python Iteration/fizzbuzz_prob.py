# this defines fizzbuzz
def fizzbuzz():
    # this means it starts at 1 and ends at 1 number below you have inputed
    for x in range(1, end+1):
        # if x /3 remainder= 0 and x /5 remainder = 0, it  prints fizzbuzz
        if x % 3 == 0 and x % 5 == 0:
            print("fizzbuzz")
           # if x / 3  remainder= 0 print fizz
        elif x % 3 == 0:
            print("Fizz")
            # if x/5  remainder = 0 it prints buzz
        elif x % 5 == 0:
            print("buzz")
            # the line belows  will print  a list of numbers which doesnt meet the statements above
        else:
            print(x)


# this is the main program with an input statement
end = int(input("type in the end number\n"))
# prints the answers
fizzbuzz()
