def fibonacci(z):
   if z <= 1:
       return z
   else:
       return(fibonacci(z-1) + fibonacci(z-2))
   
def mold(y):
    if y <= 0:
        print("Only positive number!")
    else:
       print('The-'+str(y),"fibonacci number is", fibonacci(y))

while True:
    try:
        num = int(input("Insert number : "))
    except ValueError:
        print('Invalid value entered!\n')
    else:
        mold(num)
