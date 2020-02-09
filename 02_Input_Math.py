#Get Input

#Ask user for name
name = input("What is your name?")

#ask user for two numbers
num1 = int(input("What is your favourite number? "))
num2 = int(input("What is your second favourite number? "))

#add numbers together
added = num1 + num2

#multiply numbers together
multiplied = num1 * num2

#Greet user and display results
print("Hello", name)
print("{} + {} = {}".format(num1, num2, added))
print("{} * {} = {}".format(num1, num2, multiplied))