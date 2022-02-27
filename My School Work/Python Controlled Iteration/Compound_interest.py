# I changed the code  so that i can understand and you can input any 'balance','interest rate' and 'target balance' without changing the code
# this is an input statement stored in the variable 'balance'
remaining = float(input("type in the balance\n"))
# this is an input statement stored in the variable 'interestrate'
interest = float(input("type in interest rate\n"))
# this is an input statement stored in the variable 'targetbalance'
target = float(input("type in target balance\n"))


def new_balance_calc(balance, interestrate, targetbalance):
    # the number 0 is stored in the variable 'year'
    year = 0
    #   if  'balance' is less than 'targetbalance ' then it will keep looping until the condition is false
    while balance < targetbalance:

        interest = balance*interestrate

        balance = balance + interest
    # here if the condition is true   it will add 1 to the variable year every time until the condition is false
        year = year + 1
    # the line "round(balance,2))" means the value of balance is rounded  to 2 decimal places if you change the number to 3 instead of 2 it will round the value of balance to 3 decimal places
        print("year ", year, " new balance = £", round(balance, 2))


new_balance_calc(remaining, interest, target)
