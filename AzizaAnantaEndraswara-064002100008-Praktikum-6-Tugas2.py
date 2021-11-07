print("This program will determine the number of days of a given month")
def dateMonth(bulan):
    if bulan in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
        if bulan == 2:
            tahun = int(input("Enter the year : "))
            dateYear(tahun)
        else:
            if bulan in [1, 3, 5, 7, 8, 10, 12]:
                print("There are 31 days in the month")
            else:
                print("There are 30 days in the month")
    else:
        print(f"* Invalid value entered : {bulan}")
                
def dateYear(tahun):
    if tahun%4 == 0:
        print("This is the leap year and there are 29 days in the month")
    else:
        print("There are 28 days in the month")

loop = True
while loop == True:
    print("Enter -1 to stop the program")
    bulan = int(input("Enter the month (1-12) : "))
    if bulan == -1:
        loop = False
        print("Terimakasih sudah menggunakan program saya. Sampai berjumpa lagi.")
    else:
        dateMonth(bulan)
