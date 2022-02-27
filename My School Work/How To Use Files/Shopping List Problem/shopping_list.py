# importing a library of code called operating system
import os


# this function that checks if the file exists
def file_validation():

    print("\nThe shopping list must exist \n")
    # we check if a file/shopping list exists using the function os.path.exists(path)
    whichfile = input("\nWhich shopping list would you like to open \n")

    check = os.path.exists(whichfile)
    # we get a boolean value which is assigned to the variale 'check'
    if check == False:
        return whichfile, check

    elif check == True:
        # if the user tries to open the file where i wrote my code it will not allow the user to open it and edit the code
        if whichfile == "main.py":
            print("\nNice try but no \n")
            check = False
            return whichfile, check
        else:
            return whichfile, check


# a function called 'creating_file' is called so that when the user types 1 it will call this function to create a shopping list file
# the file is opened in create mode
def creating_shopping_list():

    listname = input("\nWhat is the name of your shopping list:\n")
    # because we are opening in create mode it wont work if the file exists so we use Exceptional handaling (try : and except :). if the file exists it creates an error called 'FileExistsError' which will break the program so we use an except to not break the program
    try:
        shoppingfile = open(listname, "x")
        shoppingfile.close()
        print("\nShopping list", listname, "has been created\n")

    except FileExistsError:
        print("\nThis file exists\n")


# this function is called when the user types 2 so that the user can add items to a shopping list
def adding_item():

    count = 3
    filecheck = False
    while not filecheck:
        # calls for the function 'file_validation' to check whether the file exists or not
        whichfile, check = file_validation()
        if check == True:
            filecheck = True
            item = input("\nWhich item would you like to add\n")
            # opens the file in append mode
            shoppingfile = open(whichfile, "a")
            shoppingfile.write("{}\n".format(item))
            shoppingfile.close()
            print("\nItem", item, "has been added to shopping list", whichfile,
                  "\n")
        elif check == False:
            count = count - 1
            print(
                "\nYou only got", count,
                "chances to type in the right filename or else you will be brought back to the mainmenu\n"
            )
            # if you type the shopping lists name incorectly 3 times it will bring you back to the menu
            if count == 0:
                mainmenu()


# this function is called when the user types 3 so that the user can delete or replace an item in their shopping list
def removing_or_replace_item():

    count = 3
    filecheck = False
    while not filecheck:
        whichfile, check = file_validation()
        if check == True:
            filecheck = True
            count = 3
            # if the file exists the user is given a choice whether they want to remove a item or replace a item they choose
            choicecheck = False
            while not choicecheck:
                print("\n1. Remove item\n")
                print("\n2. Replace item\n")
                ask = int(input("\nWhich number do you choose\n"))
                if ask == 1:
                    choicecheck = True

                    def remove_item():
                        remove = input(
                            "\nWhich item would you like to remove\n")
                        # to remove the item the file is opened in read mode
                        shoppingfile = open(whichfile, "r")
                        new_file_content = ""
                        # now a for loop is used to read through the file  which is stored in the variable 'line'
                        for line in shoppingfile:
                            # we use the strip function to remove spaces between the strings in the file which is store in the variable 'stripped_line'
                            stripped_line = line.strip()
                            # we are going to remove the item the user doesnt
                            # we can do this by using the replace function which is  variable.replace(old arguement,new arguement)
                            # where the old arguement is the one you want to remove/ replace and the new arguement is the new item you want to replace or a empty string if you want to remove a item
                            # this is stored in the variable 'new_line' but then all of it is transfered to the variable 'new_file_content' with additional string then the file is closed
                            new_line = stripped_line.replace(remove, "")
                            new_file_content += new_line + "\n"
                        shoppingfile.close()
                        # the file is again opened in write mode to overwrite the existing strings this how items are removed or replaced
                        shopping = open(whichfile, "w")
                        shopping.write(new_file_content)
                        shopping.close()
                        print("\nItem", remove,
                              "has been removed from the shopping list",
                              whichfile, "\n")

                    remove_item()

                elif ask == 2:
                    # here the same thing happens as removing an item
                    # but in the replace function the new arguement is the user input which is the user's replacement item
                    choicecheck = True

                    def replace_item():
                        remove = input(
                            "\nWhich item would you like to replace\n")
                        replaced = input("\nWhat is your replacement item\n")
                        shoppingfile = open(whichfile, "r")
                        new_file_content = ""
                        for line in shoppingfile:
                            stripped_line = line.strip()
                            new_line = stripped_line.replace(remove, replaced)
                            new_file_content += new_line + "\n"
                        shoppingfile.close()
                        shopping = open(whichfile, "w")
                        shopping.write(new_file_content)
                        shopping.close()
                        print("\nItem", remove, "has been replaced to",
                              replaced, "in the shopping list", whichfile,
                              "\n")

                    replace_item()
                else:
                    count = count - 1
                    print(
                        "\nYou only got", count,
                        "chances to type in the right choice or else you will be brought back to the mainmenu\n"
                    )
                    if count == 0:
                        mainmenu()
        elif check == False:
            count = count - 1
            print(
                "\nYou only got", count,
                "chances to type in the right filename or else you will be brought back to the mainmenu\n"
            )
            # if you type the shopping lists name incorectly 3 times it will bring you back to the menu
            if count == 0:
                mainmenu()


# this function is called when the user types 4 which is to read a shopping list
def view_shoppingfile():

    count = 3
    filecheck = False
    # there is file validation
    while not filecheck:
        whichfile, check = file_validation()
        if check == False:
            count = count - 1
            print(
                "\nYou only got", count,
                "chances to type in the right filename or else you will be brought back to the mainmenu\n"
            )
            if count == 0:
                mainmenu()
        # if the file exists the file is opened and read/printed to the user using read function
        # the file is opened in read mode
        elif check == True:
            filecheck = True
            shoppingfile = open(whichfile, "r")
            print("")
            print(shoppingfile.read())


# this function is called when the user types 5 which is to rename a file
def rename_file():

    count = 3
    filecheck = False
    while not filecheck:
        whichfile, check = file_validation()
        if check == False:

            count = count - 1
            print(
                "\nYou only got", count,
                "chances to type in the right filename or else you will be brought back to the mainmenu\n"
            )

            if count == 0:
                mainmenu()
        # we use the os.rename(old arguement, new arguement) function to rename the file
        # where old arguement is the name of the old file and new arguement is the new name of the old file/arguement
        elif check == True:
            filecheck = True
            rename = input("\nWhat is the new name of the shopping list\n")
            os.rename(whichfile, rename)
            print("\nShopping list", whichfile, "has been renamed to", rename,
                  "\n")


# this function is called when the user types 6 which is to delete a shopping list
def delete_file():

    count = 3
    filecheck = False
    while not filecheck:
        whichfile, check = file_validation()

        if check == False:
            count = count - 1
            print(
                "\nYou only got", count,
                "chances to type in the right filename or else you will be brought back to the mainmenu\n"
            )

            if count == 0:

                mainmenu()
        elif check == True:
            # the user types which file/ shopping list they want to remove
            # using the function os.remove(user input/specific file) the file will be deleted
            filecheck = True
            os.remove(whichfile)
            print("")
            print(whichfile, "has been deleted\n")


print(
    "This program allows you to create a shopping list to add or remove and many more features to your list\n"
)


def mainmenu():

    # main menu where you can choose what you want to do in your shopping list
    # has validation to make the user types the number between 1 and 7
    count = 10
    repeat = True
    while repeat == True:

        print("\nMake your selection\n")
        print("\n1. Create new shopping list\n")
        print("\n2. Add an item to a specific shopping list\n")
        print(
            "\n3. Remove or replace a specific item from a specific shopping list\n"
        )
        print("\n4. View a specific shopping list\n")
        print("\n5. Rename a shopping list\n")
        print("\n6. Delete a shopping list\n")
        print("\n7. Exit program\n")
        selection = input("\nWhich number do you choose: \n")
        if selection == "1":
            # calls for the function 'creating_file()'
            creating_shopping_list()
        elif selection == "2":
            # calls for the function 'adding_item()'
            adding_item()
        elif selection == "3":
            # calls for the function 'removing_item()'
            removing_or_replace_item()
        elif selection == "4":
            # calls for the function 'view_shoppingfile()'
            view_shoppingfile()
        elif selection == "5":
            # calls for the function 'rename_file()'
            rename_file()
        elif selection == "6":
            # calls for the function 'delete_file()'
            delete_file()
        elif selection == "7":
            # exists program
            print("\nGood bye\n")
            exit()
        elif len(selection) == 0 or not selection.isnumeric() or int(
                selection) > 7 or int(selection) < 1:
            count = count - 1
            print("\n You only have", count,
                  "chances before you will get kicked out from the program\n")
            if count == 0:
                print("\nSorry, good bye\n")
                exit()


mainmenu()
