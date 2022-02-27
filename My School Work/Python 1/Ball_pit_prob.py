import math


def vol_of_ballpit_calc():

    print("Please type in your values in meters\n")
    radius_of_ballpit = float(input("What is the radius of your ball pit\n"))
    height_of_ballpit = float(input("What is the height of your ball pit\n"))
    vol_of_ballpit = 3.14 * radius_of_ballpit ** 2 * height_of_ballpit
    return vol_of_ballpit


def vol_of_ball_calc():

    print("Please type in your values in metres\n")
    radius_of_single_ball = float(
        input("What is the radius of a single ball\n"))
    vol_of_ball = (4/3) * 3.14 * radius_of_single_ball ** 3
    return vol_of_ball


def number_of_balls_calc():

    volume_of_ballpit = vol_of_ballpit_calc()
    volume_of_single_ball = vol_of_ball_calc()
    number_of_balls = (volume_of_ballpit / volume_of_single_ball) * 0.75
    print("The number of balls needed to fill the ball pit is",
          math.ceil(number_of_balls))


number_of_balls_calc()
