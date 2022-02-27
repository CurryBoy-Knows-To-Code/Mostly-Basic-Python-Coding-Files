# there was bitwise operaters but the output was weird in some of them so i didnt use it so i just used the normal method to convert such as binary addition rules, list of the place values [128,64....] and etc


def binary_input_validation():
    # this function validated our binary input
    valid_binary_input = False
    while not valid_binary_input:
        mistake = 0
        binary_number = input("Enter your 8 bit binary number\n")
        # here i make sure the binary input has 8 bits
        if len(binary_number) == 8:
            binary_number_as_integer = int(binary_number)
            while binary_number_as_integer != 0:
                # we find the remainder  to see if each digit is 1 or 0
                digit = int(binary_number_as_integer % 10)
                if (digit == 1) or (digit == 0):
                    # and if it is  then we remove the digit we checked by dividing it by 10
                    binary_number_as_integer /= 10
                else:
                    # but if it is not 1 or 0 then we break the loop and then user has to type the correct binary input again
                    mistake += 1
                    break
            if (mistake == 0):
                valid_binary_input = True
                return binary_number
            else:
                print("Invalid binary number")
        else:
            print("invalid binary number")


def denary_input_validation():
    # this function validstes the denary input
    valid_denary_input = False
    while not valid_denary_input:
        denary_number = input(
            "Enter your denary value, it should be between 1 and 255\n")
        # we check if the input isnumeric and and is between 1 and 255
        if (denary_number.isnumeric()) and (int(denary_number) >= 1) and (int(denary_number) <= 255):
            valid_denary_input = True
            denary_number = int(denary_number)
            return denary_number
        # if it doesnt meet these requirements then we ask the user to enter the denary number again
        else:
            print("Denary value must be numeric and be between 1 and 255 inclusive")


def hexadecimal_input_validation(hex_system):
    # this function validates the hex input
    valid_hexadecimal_input = False
    while not valid_hexadecimal_input:
        hexadecimal_input = input("Enter your hexadecimal value\n")
        # we split the input so that we can validated and as we split it we return the denary value of it
        first_half, second_half = hexadecimal_input[:len(
            hexadecimal_input) // 2], hexadecimal_input[len(hexadecimal_input) // 2:]
        # after splitting it we see if it exists in the dictionary and because because in the dictionary the input we split is a value and to check if the value exists we have to use dictionary.values
        if first_half in hex_system.values() and second_half in hex_system.values():
            # the we use a for loop to loop through the dictionary, we have to variables which is denary_number which is the key in the dictionary then we get the hex_value which is the value of the key in the dictionary
            # and to get the key and the value paired to it we have to use the .items() function
            for denary_number, hex_value in hex_system.items():
                if first_half == hex_value:
                    denary_number_of_first_half = denary_number
                    break
            for denary_number, hex_value in hex_system.items():
                if second_half == hex_value:
                    denary_number_of_second_half = denary_number
                    break
            return hexadecimal_input, denary_number_of_first_half, denary_number_of_second_half
        else:
            print("Invalid hexadecimal value")


def hexadecimal_to_denary(denary_number_of_first_half, denary_number_of_second_half):
    # normally to conver hex to den we take the denary of first half times that by 16 then add the denary of the second half and that is what i hqave done
    denary_number = (denary_number_of_first_half * 16) + \
        denary_number_of_second_half
    return denary_number


def denary_to_hexadecimal(denary_number, hex_system):
    # for den to hex we divide by 16 but not fully we get the quotient by using the floor division or // then to get the remainder we do modulas which is %
    hexadecimal = ""
    quotient = int(denary_number) // 16
    remainder = int(denary_number) % 16
    # the quotient and remainder gives us the denary number of each which is a key in the dictionary and if it does match then we get the corresponding value of that key
    for denary_number in hex_system:
        if quotient == denary_number:
            hexadecimal += hex_system[denary_number]
            break
    for denary_number in hex_system:
        if remainder == denary_number:
            hexadecimal += hex_system[denary_number]
            break
    # here we join the hexadecimal values
    if hexadecimal[0] == "0":
        hexadecimal = hexadecimal.replace("0", "", 1)
    return hexadecimal


def hexadecimal_to_binary(denary_number_of_first_half, denary_number_of_second_half, place_values):
    # to do hex to bin we take the first half denary value and convert it do  binary
    denary_number_of_first_half_as_binary_number = denary_to_binary(
        denary_number_of_first_half, place_values)
    denary_number_of_first_half_as_binary_number = denary_number_of_first_half_as_binary_number.replace(
        "0000", "")
    # the maximum binary number you can get 00001111 and to remove the 0000 we use the replace function
    # we do the same thing again for the  second half
    denary_number_of_second_half_as_binary_number = denary_to_binary(
        denary_number_of_second_half, place_values)
    denary_number_of_second_half_as_binary_number = denary_number_of_second_half_as_binary_number.replace(
        "0000", "")
    # we combine bith bianry input then we got the binary number
    binary_number = denary_number_of_first_half_as_binary_number + \
        denary_number_of_second_half_as_binary_number
    return binary_number


def binary_to_hexadecimal(binary_number, hex_system):
    # we split the binary number to 2 nibbles  then we convert it to a denary after that we loop through the dictionary 2 see which denary value corresponds with the hex
    hexadecimal = ""
    first_nibble, second_nibble = binary_number[:len(
        binary_number) // 2], binary_number[len(binary_number) // 2:]
    first_binary_number_from_first_nibble = "0000" + first_nibble
    second_binary_number_from_second_nibble = "0000" + second_nibble
    first_half_denary_number = binary_to_denary(
        first_binary_number_from_first_nibble)
    for denary_number in hex_system:
        if denary_number == first_half_denary_number:
            hexadecimal += hex_system[denary_number]
            break
    second_half_denary_number = binary_to_denary(
        second_binary_number_from_second_nibble)
    for denary_number in hex_system:
        if denary_number == second_half_denary_number:
            hexadecimal += hex_system[denary_number]
            break
            # we combine the hex values and you got the new hex value
    return hexadecimal


def add_binary_numbers(binary_number_1, binary_number_2):
    # so i have used the binary addition rules
    try:
        binary_number_1 = binary_number_1[::-1]
        binary_number_2 = binary_number_2[::-1]
        # this carry over list used
        carry_over_list = ["0", "0", "0", "0", "0", "0", "0", "0"]
        new_binary_number = ""
        # we use a for loop and and all the if statement have a the posibilities
        for index in range(0, len(binary_number_1)):
            if (carry_over_list[index] == "0" and binary_number_1[index] == "0" and binary_number_2[index] == "0"):
                new_binary_number += "0"
                continue
            elif (carry_over_list[index] == "0" and binary_number_1[index] == "0" and binary_number_2[index] == "1") or (carry_over_list[index] == "0" and binary_number_1[index] == "1" and binary_number_2[index] == "0") or (carry_over_list[index] == "1" and binary_number_1[index] == "0" and binary_number_2[index] == "0"):
                new_binary_number += "1"
                continue
            elif (carry_over_list[index] == "0" and binary_number_1[index] == "1" and binary_number_2[index] == "1") or (carry_over_list[index] == "1" and binary_number_1[index] == "0" and binary_number_2[index] == "1") or (carry_over_list[index] == "1" and binary_number_1[index] == "1" and binary_number_2[index] == "0"):
                new_binary_number += "0"
                carry_over_list[index + 1] = "1"
                continue
            elif carry_over_list[index] == "1" and binary_number_1[index] == "1" and binary_number_2[index] == "1":
                new_binary_number += "1"
                carry_over_list[index + 1] = "1"
                continue
        print(binary_number_1, "+", binary_number_2,
              "=", new_binary_number[::-1])
        main_menu()
        # at the end of the loop if we have to add a carry over then a IndexError will happen which means that there is a 9th bit so we know it is a overflow error
    except IndexError:
        print("We added your binary numbers which is:",
              new_binary_number[::-1], "but there is a overflow error which means that there is a 9th bit")
        main_menu()


def denary_to_binary(denary_number, place_values):
    # we just loop through the place values which is [128,64,32.......]
    binary_number = ""
    for place_value in place_values:
        # if you can divide it by the place value then we add a 1 and we keep doing this to the place value 1
        count = denary_number // place_value
        if count >= 1:
            binary_number += "1"
            denary_number -= place_value
            continue
        else:
            binary_number += "0"
    # and thats how you get your binary number
    return binary_number


def binary_to_denary(binary_number):
    # each place value doubles  so goes like 2 to the power of 0 then 1,2,3,4,5,6,7 and that is what we do but we do that with the for loop
    denary_number = 0
    binary_number = binary_number[::-1]
    for bit in range(0, len(binary_number)):
        if binary_number[bit] == "1":
            # example 2 ** 0 then next itr which is 2 ** 1, 2 ** 2 and so on
            denary_number += (2 ** bit)
    return denary_number


def main_menu():
    # this is the main menu we have our list of place values and our dictionary which contains hex values corresponding to the denary value
    place_values = [128, 64, 32, 16, 8, 4, 2, 1]
    hex_system = {
        0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5",
        6: "6", 7: "7", 8: "8", 9: "9", 10: "A", 11: "B",
        12: "C", 13: "D", 14: "E", 15: "F"}
    valid_choice = False
    while not valid_choice:
        print("Press 1 if you want to convert Binary to Denary")
        print("Press 2 if you want to convert Denary to Binary")
        print("Press 3 if you want to add Binary numbers")
        print("Press 4 if you want to convert Binary to hexadecimal")
        print("Press 5 if you want to convert hexadecimal to Binary")
        print("Press 6 if you want to convert Denary to hexadecimal")
        print("Press 7 if you want to convert hexadecimal to Denary")
        print("Press 8 if you want to quit the program")
        users_choice = input("Which number do you choose\n")
        if users_choice == "1":
            binary_number = binary_input_validation()
            denary_number = binary_to_denary(binary_number)
            print(binary_number, "in denary is:", denary_number)
        elif users_choice == "2":
            denary_number = denary_input_validation()
            binary_number = denary_to_binary(denary_number, place_values)
            print(denary_number, "in binary is:", binary_number)
        elif users_choice == "3":
            binary_number_1 = binary_input_validation()
            binary_number_2 = binary_input_validation()
            add_binary_numbers(binary_number_1, binary_number_2)
        elif users_choice == "4":
            binary_number = binary_input_validation()
            hexadecimal = binary_to_hexadecimal(binary_number, hex_system)
            print(binary_number, "in hexadecimal is", hexadecimal)
        elif users_choice == "5":
            str_copy, denary_number_of_first_half, denary_number_of_second_half = hexadecimal_input_validation(
                hex_system)
            binary_number = hexadecimal_to_binary(
                denary_number_of_first_half, denary_number_of_second_half, place_values)
            print(str_copy, "in binary is", binary_number)
        elif users_choice == "6":
            denary_number = denary_input_validation()
            hexadecimal = denary_to_hexadecimal(denary_number, hex_system)
            print(denary_number, "in hexadecimal is", hexadecimal)
        elif users_choice == "7":
            str_copy, denary_number_of_first_half, denary_number_of_second_half = hexadecimal_input_validation(
                hex_system)
            denary_number = hexadecimal_to_denary(
                denary_number_of_first_half, denary_number_of_second_half)
            print(str_copy, "in denary is", denary_number)
        elif users_choice == "8":
            print("Good bye")
            exit()
        else:
            print("Invalid choice")


main_menu()
