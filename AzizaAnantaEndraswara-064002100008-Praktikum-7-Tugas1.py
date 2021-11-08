def printprimenumber(number):
    if number > 1:
        numberdetermined(number)
    else:
        print(number, "is a prime number")
        
def numberdetermined(number):
    for z in range(2, number):
            if(number % z == 0):
                print(number, "is not a prime number")
                print(z,"x",number//z,"=", number)
                break
    else:
        print(number, "is a prime number")

loop = True
while loop == True:
    print("Enter -1 to stop the program")
    number = int(input("Enter the number you want to check : "))
    if number == -1:
        loop = False
        print("Thank you for using my program. See you next time.")
    else:
        printprimenumber(number)
