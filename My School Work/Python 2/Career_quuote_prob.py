# these are your input statements
choice = input(
    "Are you an Engineer or a Developer or a Analyst or something else ?\n ")


def quotechoice(user_choice):
    # if the input meets the condition it will execute it
    if user_choice == "Engineer":

        print("The engineer has been, and is, a maker of history.")

    elif user_choice == "Developer":

        print("Logical thinking, passion and perseverance is the paint on your palette.​")

    elif user_choice == "Analyst":

        print("Seeing what other people can’t see gives you great vision.​")

    else:
        print("I'm sorry. We could not find a quote for your job.")


quotechoice(choice)
