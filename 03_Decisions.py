#If statements
keep_going = ""
while keep_going == "":
    #ask user for input
    like_coffee = input("Do you like coffee").lower()

    if like_coffee == "yes" or like_coffee == "y":
        print("eww")
        keep_going = "no"
    elif like_coffee == "no" or like_coffee == "y":
        print("Nice")
        keep_going = "no"
    else:
        print("i dont understand")
