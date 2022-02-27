def centigrade_choice():

    F = float(input("type in how many degrees Fahrenheit​ is it\n"))

    ans1 = (F-32)/1.8

    rounded_ans1 = (round(ans1, 2))

    print("It is", rounded_ans1, "Centigrade")


def fahrenheit_choice():
    C = float(input("type in how many degrees Centigrade​ is it\n"))

    ans2 = (C*1.8)+32

    rounded_ans2 = (round(ans2, 2))

    print("It is", rounded_ans2, "Fahrenheit")


def choice():

    type_of_degree = input("do you want to find Centigrade or Fahrenheit​\n ")

    if type_of_degree == "Centigrade" or type_of_degree == "centigrade" or type_of_degree == "C" or type_of_degree == "c":
        centigrade_choice()

    elif type_of_degree == "Fahrenheit" or type_of_degree == "fahrenheit" or type_of_degree == "F" or type_of_degree == "f":
        fahrenheit_choice()


choice()
