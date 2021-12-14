input('This program created by Aziza Ananta Endraswara\nPRESS ENTER')

class collegian:
     def __init__(self):
          self._name = str()
          self._age = 0
          self._nim = str()
          self._major = str()

     def get_name(self):
         print("\nShowing name!")
         return self._name
       
     def set_name(self, a):
         print("Name has been changed!")
         self._name = str.upper(a)
  
     def del_name(self):
         del self._name
     
     name = property(get_name, set_name, del_name) 
     
     def get_age(self):
         print("\nShowing age!")
         return self._age
       
     def set_age(self, a):
         print("Age has been changed!")
         self._age = a
  
     def del_age(self):
         del self._age
     
     age = property(get_age, set_age, del_age) 
     
     def get_nim(self):
         print("\nShowing NIM!")
         return self._nim
       
     def set_nim(self, a):
         print("NIM has been changed!")
         self._nim = str(a)
  
     def del_nim(self):
         del self._nim
     
     nim = property(get_nim, set_nim, del_nim) 
     
     def get_major(self):
         print("\nShowing major!")
         return self._major
       
     def set_major(self, a):
         print("Major has been changed!")
         self._major = str.upper(a)
  
     def del_major(self):
         del self._major
     
     major = property(get_major, set_major, del_major) 
  
p = collegian()
p.name = input('Enter collegian name : ')
p.nim = input('Enter collegian NIM : ')
p.age = input('Enter collegian age : ')
p.major = input('Enter collegian major : ')

while True:
    while True:
        ops = str.upper(input('''
                              
                              
Menu:
a. Edit biodata information
b. Show biodata information
c. Out of the program
>> '''       ))
        
        if ops == 'A':
            mode = 'edit'
            break
        elif ops == 'B':
            mode = 'read'
            break
        elif ops == 'C':
            mode = 'exit'
            break
        else:
            input('\nProgram can not understand!\nPress Enter')
            
    if mode == 'edit':
        while True:
            ops = str.lower(input('''
                                  
                                  
Edit:
a. Name
b. NIM
c. Age
d. Major
e. Finish
>> '''                      ))
            
            if ops == 'a':
                p.name = input('Enter collegian name : ')
            elif ops == 'b':
                p.nim = input('Enter collegian NIM : ')
            elif ops == 'c':
                p.age = input('Enter collegian age : ')
            elif ops == 'd':
                p.major = input('Enter collegian major : ')
            elif ops == 'e':
                break
            else:
                input('\nProgram can not understand!\nPress Enter')
                
                
    elif mode == 'exit':
        input('\n\nThank you for using my program. See you next time.\nPress Enter')
        break 
           
    elif mode == 'read':
        while True:
            ops = str.lower(input('''
                                  
                                  
Tampilkan:
a. Name
b. NIM
c. Age
d. Major
e. Finish
>> '''                      ))
            
            if ops == 'a':
                input(f'{p.name}\nPress Enter')
            elif ops == 'b':
                input(f'{p.nim}\nPress Enter')
            elif ops == 'c':
                input(f'{p.age}\nPress Enter')
            elif ops == 'd':
                input(f'{p.major}\nPress Enter')
            elif ops == 'e':
                break
            else:
                input('\nProgram can not understand!\nPress Enter')
