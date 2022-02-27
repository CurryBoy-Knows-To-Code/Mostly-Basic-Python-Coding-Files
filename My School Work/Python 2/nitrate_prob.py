def nitrate_check(nitrate):

    if nitrate > 10:
        return "For " + str(nitrate) + " nitrate" + " dose is 3 ml"
    else:
        if nitrate > 2.5:
            return "For " + str(nitrate) + " nitrate" + " dose is 2 ml"
        else:
            if nitrate > 1:
                return "For " + str(nitrate) + " nitrate" + " dose is 1 ml"
            else:
                return "For " + str(nitrate) + " nitrate" + " dose 0.5 ml"


nitrate = int(input("What is the amount of nitrate\n"))
print(nitrate_check(nitrate))
