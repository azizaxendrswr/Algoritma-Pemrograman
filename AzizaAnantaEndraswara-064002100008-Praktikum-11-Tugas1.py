class collegian:
    
    total = 0
    
    def __init__(self,name,nim,year):
        self.name = str.upper(name)
        self.nim = str(nim)
        self.year = str(year)
        collegian.total += 1
        
    def biodata(self):
        return str(f'{self.name} ; {self.nim} ; {self.year}')
    
    def mold(self):
        print()
        print('Name : ',self.name)
        print('NIM : ',self.nim)
        print('Year : ',self.year)
        print()
        input(f'The number of collegian now is {collegian.total} \nPress Enter!')


while True:
    print(f'\nCollegian {(collegian.total)+1}\nEnter -1 to stop the program!')
    a = str(input('Name : '))
    if a == '-1':
        break
    b = str(input('NIM : '))
    c = str(input('Year : '))
    n = collegian(a,b,c)
    
    n.mold()
