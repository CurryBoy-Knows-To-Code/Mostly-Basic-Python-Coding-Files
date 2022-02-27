# we import a module called regex or regular expressions
import re


def email_validation():
    ValidationEmail = False
    # this validates the email of both inputs and makes sure they are not the same email
    while not ValidationEmail:
        p1email = input("what is your email player 1 ?\n")
        p2email = input("what is your email player 2 ?\n")
        # this is the pattern in a typical email
        email_format = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|net|co.uk)"

        if p1email == p2email:
            print("2 players cannot have the same email")
        # uses the the function re.search to see if the email has the same format as 'email_format'
        elif not (re.search(email_format, p1email)) or not (re.search(email_format, p2email)):
            print("player 1 or/and player 2 has invalid email")
        else:
            print("Both emails are valid")
            ValidationEmail = True
            return str(p1email), str(p2email)


def gamertag_validation():
    # validates the gamertags and checks if both gamertags are the same
    ValidationGamertag = False
    while not ValidationGamertag:
        p1gamertag = input("what is your gamertag player 1 ?\n")
        p2gamertag = input("what is your gamertag player 2 ?\n")
        if p1gamertag == p2gamertag:
            print("2 players cannot have the same gamertag")
        elif len(p1gamertag) < 5 or len(p1gamertag) > 20:
            print("Player 1 gamertag charecters should be between 5 and 20")
        elif len(p2gamertag) < 5 or len(p2gamertag) > 20:
            print("Player 2 gamertag charecters should be between 5 and 20")
        else:
            print("Both gamertags are valid")
            ValidationGamertag = True
            return str(p1gamertag), str(p2gamertag)


def get_and_add_player_data():
    p1email, p2email = email_validation()
    p1gamertag, p2gamertag = gamertag_validation()

    print("Data has been added to our database")
    # creates a file and stores players email and gamertag
    Filename = "Online player's data."
    DataFile = open(Filename, "w")
    DataFile.write("Player 1 Email : {}\n".format(p1email))
    DataFile.write("Player 1 Gamertag  : {}\n".format(p1gamertag))
    DataFile.write("\nPlayer 2 Email : {}\n".format(p2email))
    DataFile.write("Player 2 Gamertag  : {}".format(p2gamertag))
    DataFile.close()


get_and_add_player_data()
