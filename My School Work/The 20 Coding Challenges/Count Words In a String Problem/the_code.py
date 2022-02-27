# this is just a neat way of writing 'datafile = open(file,"r")'
with open("file with string.txt", "r") as datafile:
    number_of_word = 0
    for word in datafile:
        # the empty split remove spaces an just splits them
        number_of_word += (len(word.split()))


print(number_of_word)
