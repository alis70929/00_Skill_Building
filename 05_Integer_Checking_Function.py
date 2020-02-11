#Ask user for a number
# Loops question so it repeats until a valid number is entered
# make code recyclable
valid = False
error = "Whoops, please enter an integer between 1 - 10"
while not valid:
    try:
        response = int(input("Enter an integer between 1 - 10"))
        if 1 <= response <= 10:
            print(response)
            valid = True
        else:
            print(error)
            print()
    except ValueError:
        print(error)
        print()