print("Pemangkatan negatif dan positif")

def pangkat(base, power):
    if power == 0:
        return 1
    elif power < 0:
        return 1 / (base * pangkat(base, abs(power)-1))
    else:
        return base * pangkat(base, power-1)

while True:
    base = int(input("Angka : "))
    power = int(input("Pangkat : "))
    print(pangkat(base, power),"\n")
