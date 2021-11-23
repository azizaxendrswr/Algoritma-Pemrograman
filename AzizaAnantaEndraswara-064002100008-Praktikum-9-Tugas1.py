def edit():
    zy = open('mybiodata.txt','w')
    
    z1 = str(input('Name : '))
    z1 = list(z1.split(' '))
    z1c = [str.capitalize(z) for z in z1]
    z1x = ' '.join(z1c)
    z2 = str(input('Age : '))
    z3 = str.upper(input('Address : '))
    z4 = str(input('Email : '))
    z5 = str(input('Guardian Lecturer : '))
    z5 = list(z5.split(' '))
    z5c = [str.capitalize(z) for z in z5]
    z5x = ' '.join(z5c)
    
    text = str(f'''
    Name                : {z1x}
    Age                 : {z2}
    Address             : {z3}
    Email               : {z4}
    Guardian Lecturer   : {z5x}
    ''')
    
    zy.write(str(text))
    
    zy.close()

    print('File saved by name "mybiodata.txt" !')

def read():
    y = open('mybiodata.txt','r')
    for i in y:
        print(i)
        
    y.close()
    
while True:
    opsi = str.lower(input('\n\nWelcome to the Editor Biodata : \na. Edit!\nb. Read!\n\nYour Choice : \n>> '))
    if opsi == 'a':
        edit()
    elif opsi == 'b':
        read()
        input('Press enter to continue the program! ')
    else:
        print('I do not understand!')
