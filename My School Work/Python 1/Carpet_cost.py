def user_input():

    print("Please type in the values in metres and cost in £\n")
    width = float(input("What is the width of the room\n"))
    length = float(input("What is the lenght of the room\n"))
    price = float(input("What is the price of the carpet\n"))
    return width, length, price


def total_amount_of_job():

    width, length, price = user_input()
    total_cost_carpet = width * length * price
    cost_of_underlay = 3 * width * length
    cost_of_grippers = (width * 2) + (length * 2)
    fitting_fee = 50
    total_cost = total_cost_carpet + cost_of_underlay + cost_of_grippers + fitting_fee
    print("The total cost of the job for fitting the carpet is "+"£" + str(total_cost))


total_amount_of_job()
