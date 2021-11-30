titleFile = str(input("Enter the title of the file : \n >> "))
nameofFile = (f"{titleFile}.txt")
f = open(nameofFile, "w")
f.close()
print(f"{nameofFile} file has been created!")
print("Enter 'z' to quit the program!")

def write(string):
    file = open(f"{titleFile}.txt","w")
    file.write(str(string))
    file.close()

def read_Only():
    file = open(f"{titleFile}.txt", "r")
    text = file.read()
    print(text)

xyz = True
while xyz == True:
    yz = (input(""))
    if yz == "z" or yz == "Z":
        print("\nYour text has been saved!")
        x = False
    else:
        write(yz)
        read_Only()
