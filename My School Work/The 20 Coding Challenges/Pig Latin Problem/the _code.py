# move the consonent to the last letter then add ay
# make a list of vovels and letters
# loop though the word append to new list to create the word
import re
our_charecter_set = re.compile('[@_!#$%^&*().<>?/\|}{~:]')
vowels = ["A", "E", "I", "O", "U"]
consonants = ("B", "C", "D", "F", "G", "H", "J", "K", "L", "M",
              "N", "P", "Q", "R", "S", "T", "Y", "V", "X", "Z")
valid_word = False
while not valid_word:
    users_word = input("What is the word you want to convert to pig latin\n")
    length_of_word = len(users_word.split())
    if (our_charecter_set.search(users_word)) or (length_of_word > 1) or (length_of_word < 1) or users_word.isnumeric():
        print("Not a word")
    else:
        valid_word = True
        first_letter = users_word[0].upper()
        if first_letter in vowels:
            pig_latin_word = users_word + "way"
            print(users_word, "in Pig Latin is", pig_latin_word)
        elif first_letter in consonants:
            length_of_word = len(users_word)
            remove_first_letter = users_word[1:length_of_word]
            pig_latin = remove_first_letter+first_letter + "ay"
            print("The word in Pig Latin is:", pig_latin)
