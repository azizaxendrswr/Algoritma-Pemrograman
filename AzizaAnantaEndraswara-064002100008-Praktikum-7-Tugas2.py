def convert(list):
    z = sum(d * 10**i for i, d in enumerate(list[::-1]))
    return z

def definey(z):
    if z == 1:
        return 'st'
    elif z == 2:
        return 'nd'
    elif z == 3:
        return 'rd'
    else:
        return 'th'
    
def definex(z):
    result = [int(z) for z in str(number)]
    if len(result) >= 2:
        finaley = list()
        finaley.append(result[-2])
        finaley.append(result[-1])
        che = convert(finaley)
        if che == 11 or che == 12 or che == 13:
            return 'th'
        else:
            return definey(result[-1])
    else:
        return definey(z)


while True:    
    try:  
        print()
        number = int(input('Insert Number : '))
    except ValueError:
        print('Invalid value entered')
    else:
        results = definex(number)
        print(str(number)+results)
