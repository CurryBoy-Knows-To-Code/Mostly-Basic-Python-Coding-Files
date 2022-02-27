# Div zero problem
# Function to return the division of two numbers
def Divide(Number1, Number2):
    try:
        Result = Number1 / Number2
        return Result
    except:
        return "Math Error"


# Main program
print(Divide(12, 0))
