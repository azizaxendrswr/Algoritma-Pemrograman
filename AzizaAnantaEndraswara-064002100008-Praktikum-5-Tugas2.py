total = 0
while True:
    try:
        age = int(input("Enter Your Age : "))
    except ValueError:
        break
    if age <= 2:
            print("Free")
    elif age in [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
            total += 14.00
            print("Price $14.00")
            print(f"Running total : ${total}")
    elif age >= 65:
            total += 18.00
            print("Price $18.00")
            print(f"Running total : ${total}")
    else:
            total += 23.00
            print("Price $23.00")
            print(f"Running total : ${total}")
            
money = int(input("Put your money : "))
if money > total:
    pay = money - total
    print(f"Change : ${pay}")
elif money < total:
    pay = total - money
    print(f"Your money is not enough ${pay}")
else:
    print("Your money is enough. Thank You, Enjoy!")
