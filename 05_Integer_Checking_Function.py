#Ask user for a number
# Loops question so it repeats until a valid number is entered
# make code recyclable

#Functions go here
def intcheck(low,high):
    valid = False
    error = "Whoops, please enter an integer between {} - {}".format(low,high)
    while not valid:
        try:
            response = int(input("Enter a integer between {} - {}".format(low,high)))
            if low <= response <= high:
                return response
                valid = True
            else:
                print(error)
                print()
        except ValueError:
            print(error)
            print()
#Main routine goes here
num_1 = intcheck(10,20)
num_2 = intcheck(12,24)