def value_validation():
    while True:
        try:
            value = round(float(input("Enter your value\n")), 2)
            return value
        except ValueError:
            print("The input should be a number")
            continue


def conversion_currency():
    def conversion_unit_is_pounds_as_currency():
        if values_unit == "2":
            print(value, "Dollar(s) in Pound(s) is", round(value*0.73, 2))
        elif values_unit == "3":
            print(value, "Rupee(s) in Pound(s) is", round(value*0.0099, 2))
        main_menu()

    def conversion_unit_is_dollars():
        if values_unit == "1":
            print(value, "Pound(s) in Dollar(s) is", round(value*1.38, 2))
        elif values_unit == "3":
            print(value, "Rupee(s) in Dollar(s) is", round(value*0.014, 2))
        main_menu()

    def conversion_unit_is_rupees():
        if values_unit == "1":
            print(value, "Pound(s) in Rupee(s) is", round(value*100.60, 2))
        elif values_unit == "2":
            print(value, "Dollar(s) in Rupee(s) is", round(value*72.91, 2))
            pass
        main_menu()

    valid = False
    value = value_validation()
    while not valid:
        print("Press 1 for Pounds(£)")
        print("Press 2 for Dollars($)")
        print("Press 3 for Rupees(₹)")
        values_unit = input(
            "What is the unit for the value you entered, choose your number\n")
        conversion_unit = input(
            "To which unit you want to convert it to, choose your number\n")
        if values_unit == conversion_unit:
            print("Both units are the same")
        elif (values_unit.isnumeric()) and (int(values_unit) >= 1) and (int(values_unit) <= 3) and (conversion_unit.isnumeric()) and (int(conversion_unit) >= 1) and (int(conversion_unit) <= 3):
            valid = True
            if conversion_unit == "1":
                conversion_unit_is_pounds_as_currency()
            elif conversion_unit == "2":
                conversion_unit_is_dollars()
            elif conversion_unit == "3":
                conversion_unit_is_rupees()
        else:
            print("One of the values are invalid")


def conversion_length():
    def conversion_unit_is_kilometres():
        if values_unit == "2":
            print(value, "Metre(s) in Kilometre(s) is approximately",
                  round(value/1000, 2))
        elif values_unit == "3":
            print(value, "Centimetre(s) in Kilometre(s) is approximately",
                  round(value/100000, 2))
        elif values_unit == "4":
            print(value, "Millimetre(s) in Kilometre(s) is approximately",
                  round(value/1000000, 2))
        elif values_unit == "5":
            print(value, "Mile(s) in Kilometre(s) is approximately",
                  round(value*1.609, 2))
        main_menu()

    def conversion_unit_is_metres():
        if values_unit == "1":
            print(value, "Kilometre(s) in Metre(s) is approximately",
                  round(value*1000, 2))
        elif values_unit == "3":
            print(value, "Centimetre(s) in Metre(s) is approximately",
                  round(value/100, 2))
        elif values_unit == "4":
            print(value, "Millimetre(s) in Metre(s) is approximately",
                  round(value/1000, 2))
        elif values_unit == "5":
            print(value, "Mile(s) in Metre(s) is approximately",
                  round(value*1609, 2))
        main_menu()

    def conversion_unit_is_centimetres():
        if values_unit == "1":
            print(value, "Kilometre(s) in Centimetre(s) is approximately",
                  round(value*100000, 2))
        elif values_unit == "2":
            print(value, "Metre in Centimetre(s) is approximately",
                  round(value*100, 2))
        elif values_unit == "4":
            print(value, "Millimetre(s) in Centimetre(s) is approximately",
                  round(value/10, 2))
        elif values_unit == "5":
            print(value, "Mile(s) in Centimetre(s) is approximately",
                  round(value*160934, 2))
        main_menu()

    def conversion_unit_is_millimetres():
        if values_unit == "1":
            print(value, "Kilometre(s) in Millimetre(s) is approximately",
                  round(value*1000000, 2))
        elif values_unit == "2":
            print(value, "Metre(s) in Millimetre(s) is approximately",
                  round(value*1000, 2))
        elif values_unit == "3":
            print(value, "Centimetre(s) in Millimetre(s) is approximately",
                  round(value*10, 2))
        elif values_unit == "5":
            print(value, "Mile(s) in Millimetre(s) is approximately",
                  round(value*1609344, 2))
        main_menu()

    def conversion_unit_is_miles():
        if values_unit == "1":
            print(value, "Kilometre(s) in Mile(s) is approximately",
                  round(value/1.609, 2))
        elif values_unit == "2":
            print(value, "Metre(s) in Miles(s) is approximately",
                  round(value/1609, 2))
        elif values_unit == "3":
            print(value, "Centimetre(s) in Mile(s) is approximately",
                  round(value*160934, 2))
        elif values_unit == "4":
            print(value, "Millimetre(s) in Mile(s) is approximately",
                  round(value/1609344, 2))
        main_menu()

    value = value_validation()
    valid = False
    while not valid:
        print("Press 1 for Kilometres")
        print("Press 2 for Metres")
        print("Press 3 for Centimetres")
        print("Press 4 for Millimetres")
        print("Press 5 for Miles")
        values_unit = input(
            "What is the unit for the value you entered, choose your number\n")
        conversion_unit = input(
            "To which unit you want to convert it to, choose your number\n")
        if values_unit == conversion_unit:
            print("Both units are the same")
        elif (values_unit.isnumeric()) and (int(values_unit) >= 1) and (int(values_unit) <= 5) and (conversion_unit.isnumeric()) and (int(conversion_unit) >= 1) and (int(conversion_unit) <= 5):
            valid = True
            if conversion_unit == "1":
                conversion_unit_is_kilometres()
            elif conversion_unit == "2":
                conversion_unit_is_metres()
            elif conversion_unit == "3":
                conversion_unit_is_centimetres()
            elif conversion_unit == "4":
                conversion_unit_is_millimetres()
            elif conversion_unit == "5":
                conversion_unit_is_miles()
        else:
            print("One of the values are invalid")


def conversion_volume():
    value = value_validation()
    valid = False
    while not valid:
        print("Press 1 for Littres")
        print("Press 2 for Millilitres")
        values_unit = input(
            "What is the unit for the value you entered, choose your number\n")
        conversion_unit = input(
            "To which unit you want to convert it to, choose your number\n")
        if values_unit == conversion_unit:
            print("Both units are the same")
        elif (values_unit.isnumeric()) and (int(values_unit) >= 1) and (int(values_unit) <= 2) and (conversion_unit.isnumeric()) and (int(conversion_unit) >= 1) and (int(conversion_unit) <= 2):
            valid = True
            if conversion_unit == "1":
                print(value, "Millilittres in Littres is approximately",
                      round(value/1000, 2))
            elif conversion_unit == "2":
                print(value, "Littres in Millilitres is approximately",
                      round(value*1000, 2))
        else:
            print("One of the values are invalid")


def conversion_mass():
    def conversion_unit_is_tonnes():
        if values_unit == "2":
            print(value, "Kilograms in Tonnes is approximately",
                  round(value/1000, 2))
        elif values_unit == "3":
            print(value, "Grams in Tonnes is approximately",
                  round(value/1000000, 2))
        elif values_unit == "4":
            print(value, "Stone in Tonnes is approximately", round(value/157, 2))
        elif values_unit == "5":
            print(value, "Pounds in Tonnes is approximately", round(value/2205, 2))
        elif values_unit == "6":
            print(value, "Ounce in Tonnes is approximately", round(value/35274, 2))
        main_menu()

    def conversion_unit_is_kilograms():
        if values_unit == "1":
            print(value, "Tonnes in Kilograms is approximately",
                  round(value*1000, 2))
        elif values_unit == "3":
            print(value, "Grams in Kilograms is approximately",
                  round(value/1000, 2))
        elif values_unit == "4":
            print(value, "Stone in Kilograms is approximately",
                  round(value*6.35, 2))
        elif values_unit == "5":
            print(value, "Pounds in Kilograms is approximately",
                  round(value/2.205, 2))
        elif values_unit == "6":
            print(value, "Ounce in Kilograms is approximately",
                  round(value/35.274, 2))
        main_menu()

    def conversion_unit_is_grams():
        if values_unit == "1":
            print(value, "Tonnes in Grams is approximately",
                  round(value*1000000, 2))
        elif values_unit == "2":
            print(value, "Kilograms in Grams is approximately",
                  round(value*1000, 2))
        elif values_unit == "4":
            print(value, "Stone in Grams is approximately", round(value*6350, 2))
        elif values_unit == "5":
            print(value, "Pounds in Grams is approximately", round(value*454, 2))
        elif values_unit == "6":
            print(value, "Ounce in Grams is approximately", round(value*28.35, 2))
        main_menu()

    def conversion_unit_is_stone():
        if values_unit == "1":
            print(value, "Tonnes in Stone is approximately", round(value*157, 2))
        elif values_unit == "2":
            print(value, "Kilograms in Stone is approximately",
                  round(value/6.35, 2))
        elif values_unit == "3":
            print(value, "Grams in Stone is approximately", round(value/6350, 2))
        elif values_unit == "5":
            print(value, "Pounds in Stone is approximately", round(value/14, 2))
        elif values_unit == "6":
            print(value, "Ounce in Stone is approximately", round(value/224, 2))
        main_menu()

    def conversion_unit_is_pounds_as_mass():
        if values_unit == "1":
            print(value, "Tonnes in Pounds is approximately", round(value*2205, 2))
        elif values_unit == "2":
            print(value, "Kilograms in Pounds is approximately",
                  round(value*2.205, 2))
        elif values_unit == "3":
            print(value, "Grams in Pounds is approximately", round(value/454, 2))
        elif values_unit == "4":
            print(value, "Stone in Pounds is approximately", round(value*14, 2))
        elif values_unit == "6":
            print(value, "Ounce in Pounds is approximately", round(value/16, 2))
        main_menu()

    def conversion_units_is_ounces():
        if values_unit == "1":
            print(value, "Tonnes in Ounce is approximately", round(value*35204, 2))
        elif values_unit == "2":
            print(value, "Kilograms in Ounce is approximately",
                  round(value*35.274, 2))
        elif values_unit == "3":
            print(value, "Grams in Ounce is approximately", round(value/28.35, 2))
        elif values_unit == "4":
            print(value, "Stone in Ounce is approximately", round(value*224, 2))
        elif values_unit == "5":
            print(value, "Pounds in Ounce is approximately", round(value*16, 2))
        main_menu()
    value = value_validation()
    valid = False
    while not valid:
        print("Press 1 for Tonnes")
        print("Press 2 for Kilograms")
        print("Press 3 for Grams")
        print("Press 4 for Stone")
        print("Press 5 for Pounds(mass)")
        print("Press 6 for Ounces")
        values_unit = input(
            "What is the unit for the value you entered, choose your number\n")
        conversion_unit = input(
            "To which unit you want to convert it to, choose your number\n")
        if values_unit == conversion_unit:
            print("Both units are the same")
        elif (values_unit.isnumeric()) and (int(values_unit) >= 1) and (int(values_unit) <= 6) and (conversion_unit.isnumeric()) and (int(conversion_unit) >= 1) and (int(conversion_unit) <= 6):
            valid = True
            if conversion_unit == "1":
                conversion_unit_is_tonnes()
            elif conversion_unit == "2":
                conversion_unit_is_kilograms()
            elif conversion_unit == "3":
                conversion_unit_is_grams()
            elif conversion_unit == "4":
                conversion_unit_is_stone()
            elif conversion_unit == "5":
                conversion_unit_is_pounds_as_mass()
            elif conversion_unit == "6":
                conversion_units_is_ounces()
        else:
            print("One of the values are invalid")


def conversion_temperatures():
    def conversion_unit_is_Celcius():
        if values_unit == "2":
            print(value, "degree's farenheit in celsius is approximately",
                  round((value - 32) * (5/9, 2)), "degree's")
        elif values_unit == "3":
            print(value, "degree's kelvin in celsius is approximately",
                  round((value - 273.15, 2)), "degree's")
        main_menu()

    def conversion_unit_is_Farenheit():
        if values_unit == "1":
            print(value, "degree's celsius in farenheit is approximately",
                  round((value * (9/5), 2)) + 32, "degree's")
        elif values_unit == "3":
            print(value, "degree's kelvin in farenheit is approximately",
                  round((value - 273.15) * (9/5) + 32, 2), "degree's")
        main_menu()

    def conversion_unit_is_Kelvin():
        if values_unit == "1":
            print(value, "degree's celsius in kelvin is approximately",
                  round((value + 273.15, 2)), "degree's")
        elif values_unit == "2":
            print(value, "degree's farenheit in kelvin is approximately",
                  round((value - 32) * (5/9) + 273.15, 2), "degree's")
        main_menu()

    valid = False
    value = value_validation()
    while not valid:
        print("Press 1 for Celsius")
        print("Press 2 for Farenheit")
        print("Press 3 for Kelvin")
        values_unit = input(
            "What is the unit for the value you entered, choose your number\n")
        conversion_unit = input(
            "To which unit you want to convert it to, choose your number\n")
        if values_unit == conversion_unit:
            print("Both units are the same")
        elif (values_unit.isnumeric()) and (int(values_unit) >= 1) and (int(values_unit) <= 3) and (conversion_unit.isnumeric()) and (int(conversion_unit) >= 1) and (int(conversion_unit) <= 3):
            valid = True
            if conversion_unit == "1":
                conversion_unit_is_Celcius()
            elif conversion_unit == "2":
                conversion_unit_is_Farenheit()
            elif conversion_unit == "3":
                conversion_unit_is_Kelvin()
        else:
            print("One of the values are invalid")


def main_menu():
    valid_choice = False
    while not valid_choice:
        print("Press 1 if you want to convert temperature")
        print("Press 2 if you want to convert mass")
        print("Press 3 if you want to convert volume")
        print("Press 4 if you want to convert length")
        print("Press 5 if you want to convert currency")
        print("Press 6 if you want to quit the program")
        user_choice = input("Which number do you choose\n")
        if user_choice == "1":
            conversion_temperatures()
        elif user_choice == "2":
            conversion_mass()
        elif user_choice == "3":
            conversion_volume()
        elif user_choice == "4":
            conversion_length()
            pass
        elif user_choice == "5":
            conversion_currency()
            pass
        elif user_choice == "6":
            print("Good bye")
            exit()
        else:
            print("Invalid choice")


main_menu()
