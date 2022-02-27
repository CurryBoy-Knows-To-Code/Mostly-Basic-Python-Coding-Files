# Quote of the day problem
import random
# Initialise data
Quote = [["" for X in range(2)] for Y in range(3)]
# Function to output a random quote


def RandomQuote():

    Quote[0][0] = "Any fool can write code that a computer can understand.Good programmers write code that humans can understand."
    Quote[0][1] = "Martin Fowler"

    Quote[1][0] = "Code is like humour. When you have to explain it, it’s bad."
    Quote[1][1] = "Cory House"

    Quote[2][0] = "Simplicity is the soul of efficiency."
    Quote[2][1] = "Austin Freeman"

    return Quote[Index][0], Quote[Index][1]

    print("{} - {}".format(Quote, Author))


# Main program
random.seed()
# Pick a random quote
Index = random.randint(0, 2)

Quote, Author = RandomQuote()

print("{} - {}".format(Quote, Author))
