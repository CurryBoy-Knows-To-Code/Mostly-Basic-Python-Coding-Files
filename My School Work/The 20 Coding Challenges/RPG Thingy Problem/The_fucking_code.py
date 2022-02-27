# i just want to say one thing this is the most boring, time consuming program, there was nothing challenging about it the only hard part is to think what extra abilities i should add and there is nothing complicated or something new i have used so im not going to comment it
import random
import os


def view_users_RPG_charecter_in_file():
    tries = 0
    valid_existing_file = False
    while not valid_existing_file:
        users_file = input("What is the name of the file\n")
        if os.path.exists(users_file) == True:
            valid_existing_file = True
            datafile = open(users_file, "r")
            print(datafile.read())
        elif tries == 2:
            print("Sorry but we are taking you back to the main menu")
            main_menu()
        else:
            print("This file doesnt exist")
            tries += 1


def save_users_RPG_charecter_to_file(charecter_class, gender, strength, magic, dexterity_points, extra_ability):
    valid_file = False
    while not valid_file:
        users_file = input("What is the name of the file\n")
        if os.path.exists(users_file) == True:
            print("This file exists choose a different name")
        else:
            valid_file = True
            datafile = open(users_file, "w")
            datafile.write("Charecters class: {}".format(charecter_class))
            datafile.write("Charecters gender: {}".format(gender))
            datafile.write("Strength out of 10: {}".format(strength))
            datafile.write("Magic out of 10: {}".format(magic))
            datafile.write(
                "Dexterity points out of 10: {}".format(dexterity_points))
            datafile.write("Extra ability: {}".format(extra_ability))
            main_menu()


def creating_users_RPG_charecter(charecter_class, gender):
    extra_abilities = ["Attack damage increases as combos increases", "Regeneration", "Cloak of invisibility", "Ability to read minds", "Shapeshifter",
                       "The ability to use weak magic", "Absorb powers of other enemy", "Increased dexterity points", "Can bring life to the dead (create army)", ""]
    if charecter_class == "Fighter":
        strength = random.randint(8, 10)
        magic = 0
        dexterity_points = random.randint(7, 9)
        extra_ability = extra_abilities[random.randint(0, 9)]
        if extra_ability == extra_abilities[5]:
            magic += 1
        elif extra_ability == extra_abilities[7]:
            dexterity_points += 1
    elif charecter_class == "Assassin":
        strength = 7
        magic = 0
        dexterity_points = 9
        extra_ability = extra_abilities[random.randint(0, 9)]
        if extra_ability == extra_abilities[5]:
            magic += 1
        elif extra_ability == extra_abilities[7]:
            dexterity_points += 1
    elif charecter_class == "Mage":
        strength = random.randint(3, 5)
        magic = 9
        dexterity_points = random.randint(5, 7)
        extra_ability = extra_abilities[random.randint(0, 9)]
        while extra_ability == extra_abilities[5]:
            extra_ability = extra_abilities[random.randint(0, 9)]
    elif charecter_class == "Hunter":
        strength = random.randint(6, 8)
        magic = 0
        dexterity_points = random.randint(8, 10)
        extra_ability = extra_abilities[random.randint(0, 9)]
        if extra_ability == extra_abilities[5]:
            magic += 1
        elif extra_ability == extra_abilities[7]:
            dexterity_points += 1
    elif charecter_class == "Berserker":
        strength = 10
        magic = random.randint(4, 6)
        dexterity_points = random.randint(6, 8)
        extra_ability = extra_abilities[random.randint(0, 9)]
        if extra_ability == extra_abilities[5]:
            magic += 1
        elif extra_ability == extra_abilities[7]:
            dexterity_points += 1
    print("Charecter class:", charecter_class)
    print("Gender:", gender)
    print("Strength out of 10:", strength)
    print("Magic out of 10:", magic)
    print("Dexterity points out of 10:", dexterity_points)
    print("Extra Ability:", extra_ability)
    valid_choice = False
    while not valid_choice:
        choice = input("Press 1 if you want to save it or press 2 to exit")
        if choice == "1":
            # save to a File
            save_users_RPG_charecter_to_file(
                charecter_class, gender, strength, magic, dexterity_points, extra_ability)
            pass
        elif choice == "2":
            print("Good bye")
            exit()
        else:
            print("Invalid input")


def users_rules():
    tries = 0
    valid_class = False
    while not valid_class:
        print("Classes you can chose from are: Fighter, Assassin, Mage, Hunter, Berserker")
        users_class = input(
            "which class do you choose, choose the classes number or to see more information on each class type 'information'\n")
        if (users_class == "Fighter") or (users_class == "Assassin") or (users_class == "Mage") or (users_class == "Hunter") or (users_class == "Berserker"):
            valid_class = True
            tries = 0
            valid_gender_type = False
            while not valid_gender_type:
                charecters_gender = input(
                    "Type 'Male' for male and 'Female' for female\n")
                if charecters_gender == "Male" or charecters_gender == "Female":
                    valid_gender_type = True
                    creating_users_RPG_charecter(
                        users_class, charecters_gender)
                elif tries == 2:
                    print("Sorry but we are taking you back to the main menu")
                    main_menu()
                else:
                    tries += 1
                    print("Invalid input")
        elif users_class == "information":
            class_information = open("class information.txt", "r")
            print(class_information.read())
        elif tries == 2:
            print("Sorry but we are taking you back to the main menu")
            main_menu()
        else:
            tries += 1
            print("Invalid choice")


def main_menu():
    valid_choice = False
    while not valid_choice:
        print("Press 1 if you want to create a new RPG charecter")
        print("Press 2 if you want to see your RPG charecter saved in a file")
        user_choice = input("Which number do you choose\n")
        if user_choice == "1":
            valid_choice = True
            users_rules()
        elif user_choice == "2":
            valid_choice = True
            view_users_RPG_charecter_in_file()
        else:
            print("Invalid choice")


main_menu()
