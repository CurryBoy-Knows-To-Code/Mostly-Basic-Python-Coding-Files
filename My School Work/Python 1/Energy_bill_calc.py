def user_input_and_validation():
    num_check = False
    # validates the user inputs
    while not num_check:
        previous_metre_reading = input("What is your previous metre reading\n")
        current_metre_reading = input("What is your current metre reading\n")
        # checks if the user inputs are numeric
        if previous_metre_reading.isnumeric() and current_metre_reading.isnumeric():
            num_check = True
            return float(previous_metre_reading), float(current_metre_reading)
        else:
            print("invalid input for one or both inputs")


def raw_cost_energy_calc():
    # gets the inputs from the function 'user_inpur_and_validation'
    previous_reading, current_reading = user_input_and_validation()
    units_used = current_reading - previous_reading
    calorific_value = 39.3
    # calculates the kilowatt hour
    kWh = (units_used * 1.022 * calorific_value) / 3
    energy_charge = kWh * 0.0284
    # rounds the energy_charge to 2 decimal places
    x = round(energy_charge, 2)
    print("The raw cost of energy usage is " + "£" + str(x))


raw_cost_energy_calc()
