#Ask user for a number
# Loops question so it repeats until a valid number is entered
# make code recyclable
valid = False
error = "Whoops, please enter an integer"
while not valid:
    try:
        response = int(input("Enter an integer between 1 - 10"))
        valid = True
    except ValueError:
        print(error)