num = int(input("Type in the number you want to find the square root of\n"))
# the value of root is equal to x but  the value of root can be replaced


def num_root_calc(x):
    root = x
    # the while statement means that if the value of x divided by the value of root is not equal to root  then execute the line below
    while 0.5*(root+(x/root)) != root:
        # when this line is executed the value of root is replaced with new value of root and then the new value of root is checked in the while loop statement and it will keep doing this until x divided by root is equal to root
        root = 0.5*(root+(x/root))
    # this line prints out the answer
    print("The root of", x, "is", root,)


num_root_calc(num)
