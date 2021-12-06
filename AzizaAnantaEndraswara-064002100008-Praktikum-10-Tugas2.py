def bubbleSort(z):
    count = 0
    for idx in range(len(z)-1):
        if z[idx] > z[idx + 1]:
            z[idx],z[idx + 1] = z[idx + 1],z[idx]
            count += 1
    if count == 0:
        return z
    else:
        bubbleSort(z)

while True:
    while True:
        try:        
            sort = str(input('Insert number : (a,b,c,...)\n~>>> ')).split(',')
            sort = [int(i) for i in sort]
        except:
            print('\nInvalid value entered!\n*Not an integer!')
        else:
            break
    
    print(f'\nList: {sort}')
    
    bubbleSort(sort)
    
    print(f'\nList*: {sort}')
