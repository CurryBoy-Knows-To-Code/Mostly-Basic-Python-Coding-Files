# Guess the number problem​
import random
guess_num = int(input("till what number you want to guess up too\n"))
# Function to return valid input​


def getinput():
    validinput = False
    while not validinput:
        number = input("Enter your guess\n")
# Type check​
        if number.isnumeric():
            validinput = True
    return int(number)

# Subroutine to play guess the number​


def guessthenumber(x):

    # Initialise variables​
    random.seed()

    CPU = random.randint(1, x)

    playerguess = 0

    guesscount = 0
# Continue playing until player wins​
    while playerguess != CPU:
        playerguess = getinput()

        guesscount = guesscount + 1
# Check if guess is too high or low​
        if playerguess < CPU:
            print("Too low")
        elif playerguess > CPU:
            print("TOO high")
    print("you got it, i chose", CPU, "and it took you", guesscount, "guesses")


# Main program​
guessthenumber(guess_num)
