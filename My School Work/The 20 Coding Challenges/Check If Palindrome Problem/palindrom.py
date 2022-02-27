def check(str):
    # basically this reverses the string
    if str[::-1] == str:
        return ("This is a palindrome")
    else:
        return ("This is not a palindrome")


string = "RACE   CAr"
new_string = string.replace(" ", "")

print(check(new_string.lower()))
