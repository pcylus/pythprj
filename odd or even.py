#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user
print("Odd or Even Checker \n")
print("Please Enter a valid number")
try:
    num = input("Number = ")
    if(num %2 == 0):
        print("Entered number is even")
    elif(num % 2 != 0):
        print("Number is odd")
except NameError:
    print("Please try again ")

