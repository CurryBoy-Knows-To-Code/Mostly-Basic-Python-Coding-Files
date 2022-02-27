import random


def random_dice():
    chance = False
    score = 0

    while not chance:

        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)

        if die1 == die2:
            print("your score is 0 because die 1 is equal to die 2")
            chance = True

        elif die1 != die2:
            score = score + die1 + die2

            print(die1, "+", die2,)
            print("your score is:", score)
            ask = input("another go \n")

            if ask == "YES" or ask == "Yes" or ask == "yes" or ask == "Y" or ask == "y":
                pass

            else:
                chance = True
                print("bye")


random_dice()
