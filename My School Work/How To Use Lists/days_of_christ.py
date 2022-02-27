def lists():
    # what day it is stored in the variable 'days'
    days = ["first", "second", "third", "fourth", "fifth", "sixth",
            "seventh", "eighth", "ninth", "tenth", "eleventh", "twelvth"]
    # gifts of the song are strored in the variable 'giftlist'
    giftlist = ["partridge in a pear tree\n", "turtle doves", "french hens", "calling birds", "gold rings", "geese a laying",
                "swans a swimming", "maids a milking", "ladies dancing", "lords of leaping", "pipers piping", "drummers drumming"]
    return days, giftlist


def print_carol():
    days, giftlist = lists()
    # this for loop that starts at 1 and ends at 12 which is stored in the variable 'day'
    for day in range(1, 13):
        # when this for loop is executed it prints the print statement and the days[day-1] means that the list goes down by 1 example the range starts a third then second then first it goes down by 1 like how the song goes - 3 french hens,2 calling birds, 1 partridge in a pear tree but it doesnt print out the gift list
        print("On the", days[day-1],
              "day of Christmas my true love gave to me")

        # this for loop prints out the gift list and the same thing happens as above
        for gift in range(day, 0, -1):
            # prints the giftlist in reverse
            print(gift, giftlist[gift-1])


print_carol()
