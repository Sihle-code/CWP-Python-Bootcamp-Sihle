# Options for the user 
print("1 - Add")
print("2 - Subtract")
print("3 - Multiply")
print("4 - Divide")

# Ask User to choose an operation
option = int(input("Choose an operation:"))
# division by 0
result = 0

if(option in [1,2,3,4]):
    num1 = float(input("Enter first number"))
    num2 = float(input("Enter second number"))

# add operators
    if(option == 1):
        result = num1 + num2
    elif (option == 2):
        result = num1 - num2
    elif(option == 3):
        result = num1 * num2
    elif(option == 4):
        result = num1 / num2

else:
    print("Invalid operation entered")

print("The result of the operation is {}".format(result))
