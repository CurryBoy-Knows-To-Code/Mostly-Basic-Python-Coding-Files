
name = input("What is you name\n")


def mainmenu():

    score1 = 0

    tscore1 = 10

    score2 = 0

    tscore2 = 10

    score3 = 0

    tscore3 = 26

    print("                                            ooooooooooooooooooooooooooooooooooooooooooooooooooo")
    print("                                            o                                                 o")
    print("                                            o                                                 o")
    print("                                            o      Hi",
          name, "welcome to sanjeev's fun game   o")
    print("                                            o                                                 o")
    print("                                            o                                                 o")
    print("                                            o  if you want to play true or false, press 1     o")
    print("                                            o                                                 o")
    print("                                            o  if you want to play genaral knowledge, press 2 o")
    print("                                            o                                                 o")
    print("                                            o  if you want to play the crazy quiz, press 3    o")
    print("                                            o                                                 o")
    print("                                            o                YOU  DECIDE                      o")
    print("                                            o              WHAT   YOU    DO                   o")
    print("                                            o                                                 o")
    print("                                            o    press 4 if you want to know my secret        o")
    print("                                            ooooooooooooooooooooooooooooooooooooooooooooooooooo")
    print("")

    print("")

    x = int(input("what number do you choose \n"))

    if x == 1:

        print("")

        print("Hi", name, "and you have chosen true or false and lets see if you can beat this quiz.")

        print("")
        print("There are 10 question,and each question is worth 1 point ")

        print("")

        print("Please type your answers in capital letters either TRUE or FALSE.")

        print("")

        print("Question 1")

        print("")

        q1 = input("Do earth worms breath through their skin?\n")

        print("")

        if q1 == "TRUE":

            score1 = score1 + 1

            print(q1, "is the right answer.")

            print("")

            print("Your current score is", score1,)

        else:

            print("You got the wrong answer,it is true.")

            print("")

            print("Your current score is", score1,)

        print("")

        print("Question 2")

        print("")

        q2 = input("Does the queen need a passport to travel around the world\n")

        print("")

        if q2 == "FALSE":

            score1 = score1 + 1

            print(q2, "is the right answer")

            print("")

            print("your current score is", score1,)

        else:

            print("you got the wrong answer,it is  False")

            print("")

            print("your current score is", score1,)

        print("")

        print("Question 3 ")

        print("")

        q3 = input("Do ants live up to 30 years\n")

        print("")

        if q3 == "TRUE":

            print(q3, "is the right answer")

            score1 = score1 + 1

            print("")

            print("your current score is", score1,)

        else:

            print("you got the wrong answer,it is True")

            print("")

            print("your current score is", score1,)

        print("")

        print("Question 4")

        print("")

        q4 = input("Do cuckoos  build  their own nest\n")

        print("")

        if q4 == "FALSE":

            print(q4, "is the right answer")

            score1 = score1 + 1

            print("")

            print("your current score is", score1,)

        else:

            print("you got the wrong answer,it is False")

            print("")

            print("your current score is", score1,)

        print("")

        print("Question 5")

        print("")

        q5 = input("The protagonist is the main character of a story? \n")

        print("")

        if q5 == "TRUE":
            print(q5, "is the right answer")

            print("")

            score1 = score1 + 1

            print("your current score is", score1,)

        else:

            print("you got the wrong answer,it is True")

            print("")

            print("your current score is", score1,)

        print("")

        print("Question 6")

        print("")

        q6 = input("Istanbul is the capital of Turkey? \n")

        print("")

        if q6 == "FALSE":

            print(q6, "is the right answer")

            print("")

            score1 = score1 + 1

            print("your current score is", score1,)

        else:

            print("you got the wrong answer,it is False")

            print("")

            print("your current score is", score1,)

        print("")

        print("Question 7")

        print("")

        q7 = input("Hummingbird is the only bird that cannot walk?\n")

        print("")

        if q7 == "TRUE":

            print(q7, "is the right answer")

            print("")

            score1 = score1 + 1

            print("your current score is", score1,)

        else:

            print("you got the wrong answer,it is True")

            print("")

            print("your current score is", score1,)

        print()

        print("Question 8")

        print("")

        q8 = input("Hydrogen is the most abundant element of the universe?\n")

        print("")

        if q8 == "TRUE":

            print(q8, "is the right answer")

            print("")

            score1 = score1 + 1

            print("your current score is", score1,)

        else:

            print("you got the wrong answer,it is True")

            print("")

            print("your current score is", score1,)

        print()

        print("Question 9")

        print("")

        q9 = input("Does the human heart have 6 six chambers? \n")

        print("")

        if q9 == "FALSE":

            print(q9, "is the right answer")

            print("")

            score1 = score1 + 1

            print("your current score is", score1,)

        else:

            print("you got the wrong answer,it is False")

            print("")

            print("your current score is", score1,)

        print("")

        print("Question 10")

        print("")

        q10 = input(
            "The kidney is the muscular organ that pumps blood in the human body? \n")

        print("")

        if q10 == "FALSE":

            print(q10, "is the right answer")

            print("")

            score1 = score1 + 1

            print("your current score is", score1,)

        else:

            print("you got the wrong answer,it is False")

            print("")

            print("your current score is", score1,)

            print("")

        percentage1 = (score1/tscore1)*100

        rpercentage1 = (round(percentage1, 2))

        print("you scored", rpercentage1, "%")

        if rpercentage1 <= 25:

            print("YOU ARE STUPID!!!!")

        elif rpercentage1 > 25 and rpercentage1 <= 50:

            print("YOUR IQ IS BELOW AVERAGE")

        elif rpercentage1 > 50 and rpercentage1 <= 75:

            print("YOU IQ IS EQUIVALANT TO THE AVERAGE PERSON ")

        elif rpercentage1 > 75 and rpercentage1 <= 100:

            print("YOU IQ IS ABOVE THE AVERAGE PERSON ")

            print("Well done")

            print("")

        repeat = input("would you like to go back the main menu\n").lower()

        if repeat == "Yes" or repeat == "yes" or repeat == "YES":

            mainmenu()

        else:

            print("Good bye")

            exit()

    elif x == 2:
        print("")

        print("Hi", name, "and you have chosen general knoledge and lets see if you can beat this quiz.")

        print("")

        print("There are 10 question,and each question is worth 1 point ")

        print("")
        print("Please type your answers in capital letters and in correct spelling.")

        print("")

        print("Question 1")

        print("")

        q1 = input("Who was the first American president?\n")

        print("")

        if q1 == "GEORGE WASHINGTON":

            score2 = score2 + 1

            print(q1, "is the right answer.")

            print("")

            print("Your current score is", score2,)

        else:

            print("You got the wrong answer,the right answer is GEORGE WASHINGTON.")

            print("")

            print("Your current score is", score2,)

        print("")

        print("Question 2")

        print("")

        q2 = input("Which place in the world is the happiest in the world?\n")

        print("")

        if q2 == "DISNEY WORLD":

            score2 = score2 + 1

            print(q2, "is the right answer")

            print("")

            print("your current score is", score2,)

        else:

            print("you got the wrong answer,the right answer is DISNEY WORLD")

            print("")

            print("your current score is", score2,)

        print("")

        print("Question 3")

        print("")

        q3 = int(input("How many bones does a shark have?\n"))

        print("")

        if q3 == 0:

            print(q3, "is the right answer")

            score2 = score2 + 1

            print("")

            print("your current score is", score2,)

        else:

            print("you got the wrong answer,the right answer is 0")

            print("")

            print("your current score is", score2,)

        print("")

        print("Question 4")

        print("")

        q4 = input("In what country were the olympic games invented?\n")

        print("")

        if q4 == "GREECE":

            print(q4, "is the right answer")

            score2 = score2 + 1

            print("")

            print("your current score is", score2,)

        else:

            print("you got the wrong answer,the right answer is GREECE")

            print("")

            print("your current score is", score2,)

        print("")

        print("Question 5")

        print("")

        q5 = input("What is the hardest natural substance?\n")

        print("")

        if q5 == "DIAMOND":

            print(q5, "is the right answer")

            print("")

            score2 = score2 + 1

            print("your current score is", score2,)

        else:

            print("you got the wrong answer,the right answer is DIAMOND ")

            print("")

            print("your current score is", score2,)

        print("")

        print("Question 6")

        print("")

        q6 = input("What is the most eaten food in the world ?\n")

        print("")

        if q6 == "RICE":

            print(q6, "is the right answer")

            print("")

            score2 = score2 + 1

            print("your current score is", score2,)

        else:

            print("you got the wrong answer,the right answer is RICE")

            print("")

            print("your current score is", score2,)

        print("")

        print("Question 7")

        print("")

        q7 = input("what kind of animal in ICE age is Sid \n")

        print("")

        if q7 == "SLOTH":

            print(q7, "is the right answer")

            print("")

            score2 = score2 + 1

            print("your current score is", score2,)

        else:

            print("you got the wrong answer,the right answer is SLOTH")

            print("")

            print("your current score is", score2,)

        print("")

        print("Question 8")

        print("")

        q8 = input("Where is Paddington from? \n")

        print("")

        if q8 == "PERU":

            print(q8, "is the right answer")

            print("")

            score2 = score2 + 1

            print("your current score is", score2,)

        else:

            print("you got the wrong answer,the right answer is PERU")

            print("")

            print("your current score is", score2,)

        print("")

        print("Question 9")

        print("")

        q9 = input("What colour is a giraffes tongue \n")

        print("")

        if q9 == "BLACK":

            print(q9, "is the right answer")

            print("")

            score2 = score2 + 1

            print("your current score is", score2,)

        else:

            print("you got the wrong answer,the right answer is BLACK")

            print("")

            print("your current score is", score2,)

        print("")

        print("Question 10")

        print("")

        q7 = input("What is the capital of India? \n")

        print("")

        if q7 == "NEW DELHI":

            print(q7, "is the right answer")

            print("")

            score2 = score2 + 1

            print("your current score is", score2,)

        else:

            print("you got the wrong answer,the right answer is  NEW DELHI")

            print("")

            print("your current score is", score2,)

        percentage2 = (score2/tscore2)*100

        rpercentage2 = (round(percentage2, 2))

        print("you scored", rpercentage2, "%")

        if rpercentage2 <= 25:

            print("YOU ARE STUPID!!!!")

        elif rpercentage2 > 25 and rpercentage2 <= 50:

            print("YOUR IQ IS BELOW AVERAGE")

        elif rpercentage2 > 50 and rpercentage2 <= 75:

            print("YOU IQ IS EQUIVALANT TO THE AVERAGE PERSON ")

        elif rpercentage2 > 75 and rpercentage2 <= 100:

            print("YOU IQ IS ABOVE THE AVERAGE PERSON ")

            print("Well done")

            print("")

        repeat = input("would you like to go back the main menu\n").lower()

        if repeat == "Yes" or repeat == "yes" or repeat == "YES":

            mainmenu()

        else:

            print("Good bye")

            exit()

    elif x == 3:

        print("")

        print("Hi", name, "and you have chosen the crazy quiz and lets see if you can beat this quiz.")

        print("")

        print("There are 7 question,and each question is worth 1 point ")

        print("")

        print("Please type your answers in capital letters and in correct spelling.")

        print("")

        print("Question 1")

        print("")

        q1 = input("What is the fastest car?\n")

        print("")

        if q1 == "SSC TUATARA":

            score3 = score3 + 1

            print(q1, "is the right answer.")

            print("")

            print("Your current score is", score3,)

        else:

            print("You got the wrong answer,the right answer is SSC TUATARA.")

            print("")

            print("Your current score is", score3,)

        print("")

        # this is question 2 and checks the input if it meets the if statement and it calculates the score depending what you have inputed
        print("Question 2")

        print("")

        q2 = input("Who is the author of Macbeth(his last name)\n")

        print("")

        if q2 == "SHAKESPEARE":

            score3 = score3 + 1

            print(q2, "is the right answer")

            print("")

            print("your current score is", score3,)

        else:

            print("you got the wrong answer,the right answer is SHAKESPEARE")

            print("")

            print("your current score is", score3,)

        print("")

        print("Question 3 and btw this is a math question")

        print("")

        q3 = int(input("Convert  2.35 X 10**25 into normal numbers\n"))

        print("")

        if q3 == 23500000000000000000000000:

            print(q3, "is the right answer")

            score3 = score3 + 1

            print("")

            print("your current score is", score3,)

        else:

            print(
                "you got the wrong answer,the right answer is 23500000000000000000000000")

            print("")

            print("your current score is", score3,)

        print("")

        # this is part of question 3 and checks the input if it meets the if statement and it calculates the score depending what you have inputed
        b3 = input("type this value in words to get bonus points\n")

        print("")

        if b3 == "TWENTY THREE SEPTILLION FIVE HUNDRED SEXTILLION":

            print(b3, "is the right answer!!!!!")

            score3 = score3 + 5

            print("")

            print("your current score is", score3,)

        else:

            print(
                "you got the wrong answer,the right answer is TWENTY THREE SEPTILLION FIVE HUNDRED SEXTILLION ")

            print("")

            print("your current score is", score3,)

        print("")

        print("Question 4")

        print("")

        q4 = input("What does MTB stand for\n")

        print("")

        if q4 == "MOUNTAIN BIKE":

            print(q4, "is the right answer")

            score3 = score3 + 1

            print("")

            print("your current score is", score3,)

        else:

            print("you got the wrong answer,the right answer is MOUNTAIN BIKE")

            print("")

            print("your current score is", score3,)

        print("")

        print("Question 5")

        print("")

        q5 = input(
            "What does light amplification by stimulated emission of radiation stand for\n")

        print("")

        if q5 == "LAZER":

            print(q5, "is the right answer")

            print("")

            score3 = score3 + 1

            print("your current score is", score3,)

        else:

            print("you got the wrong answer,the right answer is LAZER")

            print("")

            print("your current score is", score3,)

        print("")

        print("Question 6")

        print("")

        print("Find the document named who is this and answer the question")

        print("")

        q6 = input(" What is you answer for question 6\n")

        print("")

        if q6 == "BANSKY":

            print(q6, "is the right answer")

            print("")

            score3 = score3 + 1

            print("your current score is", score3,)

        else:

            print("you got the wrong answer,the right answer is BANSKY")

            print("")

            print("your current score is", score3,)

        print("")

        print("This is the last question which is worth 15 points but if you get it wrong you lose 5 points")

        print("")

        print("Question 7")

        print("")

        q7 = int(input("what is quattuordecillion in numbers\n"))

        print("")

        if q7 == 1000000000000000000000000000000000000000000000:

            print(q7, "is the right answer")

            print("")

            score3 = score3 + 15

            print("your current score is", score3,)

        else:

            print(
                "you got the wrong answer,the right answer is 1000000000000000000000000000000000000000000000")

            print("")

            print("your current score is", score3,)

        percentage3 = (score3/tscore3)*100

        rpercentage3 = (round(percentage3, 2))

        print("you scored", rpercentage3, "%")

        if rpercentage3 <= 25:

            print("YOU ARE STUPID!!!!")

        elif rpercentage3 > 25 and rpercentage3 <= 50:

            print("YOUR IQ IS BELOW AVERAGE")

        elif rpercentage3 > 50 and rpercentage3 <= 75:

            print("YOU IQ IS EQUIVALANT TO THE AVERAGE PERSON ")

        elif rpercentage3 > 75 and rpercentage3 <= 100:

            print("YOU IQ IS ABOVE THE AVERAGE PERSON ")

            print("Well done")

            print("")

        repeat = input("would you like to go back the main menu\n").lower()

        if repeat == "Yes" or repeat == "yes" or repeat == "YES":

            mainmenu()

        else:

            print("Good bye")

            exit()

    elif x == 4:

        print("I see you want to know my secret but if you want to know my secret you must answer 2 of my riddles and type in  THE PASSWORD ")

        choice = input("do you want to continue\n")

        if choice == "YES" or choice == "Yes" or choice == "yes":

            print("Ok and answer the questions")

            print("")

            print("Pls type your answers in capital letters")

            print("")

            print("Riddle 1")

            riddle1 = input(
                " The man who invented it doesn't want it. The man who bought it doesn't need it. The man who needs it doesn't know it. What is it?\n")

            if riddle1 == "A COFFIN" or riddle1 == "COFFIN":

                print("Ok")

            else:

                print("Ok")

            riddle2 = input(
                "I reach for the sky, but clutch to the ground; sometimes I leave, but I am always around. What am I?\n")

            if riddle2 == "A TREE" or riddle2 == "TREE":

                print("Ok")

            else:

                print("Ok")

            password = int(input(
                "pls type in 5 digit passcode and that 5 digit passcode is somewhere in this page\n"))

            if password == 13240:

                print("Ok")

            else:
                print("Ok")

            if riddle1 == "A COFFIN" or riddle1 == "COFFIN" and riddle2 == "A TREE" or riddle2 == "TREE" and password == 13240:
                print("Congratulations you can know my secret")
                print("Click this link ")
                print("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

            else:
                print("sorry you lose")

                print(name, " you will always wonder what is my secret")

                main = int(
                    input("type 1 to take your self back to the main menu\n"))

                if main == 1:

                    mainmenu()

                else:

                    print("Good bye")

                    exit()
        else:

            print(name, " you will always wonder what is my secret")

            main = int(
                input("type 1 to take your self back to the main menu\n"))

            if main == 1:

                mainmenu()

            else:

                print("Good bye")

                exit()


mainmenu()
