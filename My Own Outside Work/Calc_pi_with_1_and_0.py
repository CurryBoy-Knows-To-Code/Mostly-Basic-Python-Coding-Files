# estimate pi given that you have a function that can generate a number between 0 and 1
# from math import sqrt basically imports a specific part which is sqrt in the library math
from math import sqrt
import random


def estimate_pi(number_of_points):
    number_of_points_in_circle = 0
    number_of_points_in_total = 0

    for x in range(int(number_of_points)):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        distance = sqrt(x**2 + y**2)

        if distance <= 1:
            number_of_points_in_circle += 1

        number_of_points_in_total += 1
    print(4*(number_of_points_in_circle/number_of_points_in_total))


valid = False
while not valid:
    print("Higher number of points means a more accurate estimate of pi")
    user_input = input("Enter number of points\n")

    if user_input.isnumeric():
        estimate_pi(user_input)
    else:
        print("Only enter a number")
