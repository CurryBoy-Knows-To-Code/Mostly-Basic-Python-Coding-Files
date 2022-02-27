def user_inputs_and_validaton():
    while True:
        try:
            dmetre = float(input("Enter the diametre in cm\n"))
            angle = float(input("Enter the angle\n"))
            return dmetre, angle
        except ValueError:
            print("Invalid input")


def circle_calc():

    dmetre, angle = user_inputs_and_validaton()
    # how to calculate the following of a circle
    radius = dmetre / 2

    area = 3.14 * radius**2

    circumference = 3.14 * dmetre

    arc_length = circumference * angle / 360

    area_of_sector = (angle / 360) * area

    # show the following values of the circle
    print("the radius of the circle is:", round(radius, 2))

    print("the area of the circle is:", round(area, 2))

    print("the circumference of the circle is:", round(circumference, 2))

    print("the arc length of the circle is:", round(arc_length, 2))

    print("The area of sector is:", round(area_of_sector, 2))


circle_calc()
