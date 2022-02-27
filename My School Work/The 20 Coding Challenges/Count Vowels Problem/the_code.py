
vowels = ["A", "E", "I", "O", "U"]
sum_of_each_vowel = [0, 0, 0, 0, 0]


def check_and_count_the_vowels(users_string):
    check_string = users_string.upper()
    for index in range(0, 5):
        sum_of_each_vowel[index] = check_string.count(vowels[index])


string = input("Enter your string\n")
check_and_count_the_vowels(string)

for index in range(0, 5):
    print(vowels[index], ":", str(sum_of_each_vowel[index]))
