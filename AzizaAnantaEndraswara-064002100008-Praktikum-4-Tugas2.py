print("This program will determine the number of days of a given month")
loop = True
while loop == True:
    print("Enter -1 to stop the program")
    month = int(input("Enter the month (1-12) : "))
    if month == -1:
        loop = False
        print("Terimakasih sudah menggunakan program saya. Sampai berjumpa lagi.")
    else:
        if month in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
            if month == 2:
                year = int(input("Enter the year : "))
                if (year % 4 == 0):
                    print("This is the leap year and there are 29 days in the month")
                else:
                    print("There are 28 days in the month")
            else:
                if month in [1, 3, 5, 7, 8, 10, 12]:
                    print("There are 31 days in the month")
                else:
                    print("There are 30 days in the month")
        else:
            print(f"* Invalid value entered : {month}")
